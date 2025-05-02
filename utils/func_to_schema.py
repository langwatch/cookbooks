import inspect
from typing import Callable, Dict, Any, Optional, Union, get_type_hints, get_origin, get_args

def func_to_schema(func: Callable, description: str = None, strict: bool = True) -> Dict[str, Any]:
    """
    Convert a Python function to an OpenAI function schema.
    
    Args:
        func: The Python function to convert
        description: Description of what the function does
        strict: Whether to enforce strict mode
        
    Returns:
        A dictionary representing the OpenAI function schema
    """
    # Get function signature and docstring
    sig = inspect.signature(func)
    doc = inspect.getdoc(func) or ""
    func_name = func.__name__
    
    # Use provided description or extract from docstring
    if description is None:
        # Extract first line of docstring as description
        description = doc.strip().split('\n')[0] if doc else f"Function {func_name}"
    
    # Build parameters schema
    properties = {}
    required = []
    
    # Get type hints
    type_hints = get_type_hints(func)
    
    for param_name, param in sig.parameters.items():
        # Skip self parameter for methods
        if param_name == 'self':
            continue
            
        param_type = type_hints.get(param_name, Any)
        param_doc = _extract_param_doc(doc, param_name)
        
        # Check if parameter has a default value
        has_default = param.default is not param.empty
        
        # Build parameter schema
        param_schema = _type_to_schema(param_type, has_default)
        
        # Add description if available
        if param_doc:
            param_schema["description"] = param_doc
            
        properties[param_name] = param_schema
        
        # Add to required list if no default value and strict mode
        if not has_default and strict:
            required.append(param_name)
    
    # Create the full schema
    schema = {
        "type": "function",
        "name": func_name,
        "description": description,
        "parameters": {
            "type": "object",
            "properties": properties,
        },
        "strict": strict
    }
    
    # Add required fields and additionalProperties for strict mode
    if strict:
        schema["parameters"]["required"] = required
        schema["parameters"]["additionalProperties"] = False
    
    return schema


def _extract_param_doc(docstring: str, param_name: str) -> Optional[str]:
    """Extract parameter description from docstring."""
    if not docstring:
        return None
        
    lines = docstring.split('\n')
    param_marker = f"{param_name}:"
    
    for line in lines:
        if param_marker in line:
            desc = line.split(param_marker)[1].strip()

            return desc
    
    return None


def _type_to_schema(type_hint: Any, has_default: bool) -> Dict[str, Any]:
    """Convert Python type hint to JSON schema type."""
    # Handle None or Any
    if type_hint is None or type_hint is Any:
        return {"type": "object"}
    
    # Handle Union types (including Optional)
    origin = get_origin(type_hint)
    if origin is Union:
        args = get_args(type_hint)
        
        # Handle Optional (Union with NoneType)
        if type(None) in args:
            non_none_args = [arg for arg in args if arg is not type(None)]
            if len(non_none_args) == 1:
                schema = _type_to_schema(non_none_args[0], True)
                if "type" in schema and schema["type"] != "object":
                    schema["type"] = [schema["type"], "null"]
                return schema
        
        # General union - use anyOf
        return {
            "anyOf": [_type_to_schema(arg, has_default) for arg in args]
        }
    
    # Handle List types
    if origin is list or type_hint is list:
        item_type = Any
        if origin is list and get_args(type_hint):
            item_type = get_args(type_hint)[0]
        return {
            "type": "array",
            "items": _type_to_schema(item_type, True)
        }
    
    # Handle Dict types
    if origin is dict or type_hint is dict:
        return {"type": "object"}
    
    # Handle basic types
    basic_types = {
        str: "string",
        int: "integer",
        float: "number",
        bool: "boolean"
    }
    
    for py_type, json_type in basic_types.items():
        if type_hint is py_type:
            return {"type": json_type}
    
    # Default to object for complex types
    return {"type": "object"}
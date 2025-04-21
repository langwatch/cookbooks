# RAG Agent: Systematic Improvement Cookbook

This directory contains a systematic approach to building, evaluating, and improving Retrieval-Augmented Generation (RAG) agents. The notebooks guide you through the process of creating evaluation datasets, implementing RAG agents, and systematically measuring and improving their performance.

## Overview

Retrieval-Augmented Generation (RAG) combines retrieval systems with generative AI to create more accurate, relevant, and grounded outputs. This cookbook takes you through a methodical approach to building and optimizing RAG systems, from establishing evaluation frameworks to implementing advanced techniques.

## Notebook Structure

### 1. Data Engineering (`01_data_engineering.ipynb`)
- Creating synthetic evaluation datasets
- Analyzing dataset diversity and quality
- Establishing evaluation metrics
- Preparing data for agent testing

### 2. Agent Implementation (`02_agent_implementation.ipynb`)
- Building a complete RAG agent architecture
- Implementing adaptive retrieval strategies
- Systematic evaluation across configurations
- Visualizing performance improvements
- Establishing a framework for continuous improvement

## Key Components

The RAG agent implementation includes several key components:

- **Retriever**: Fetches relevant documents based on a query
- **Evaluator**: Assesses the quality of retrieved documents
- **Query Reformulator**: Rewrites queries to improve retrieval
- **Decision Maker**: Determines when to stop iterating
- **Answer Generator**: Creates the final response

## Usage

Start with the notebooks in sequential order. Each notebook builds upon concepts and code from previous ones.

```bash
jupyter lab
```

## Requirements

- Python 3.8+
- OpenAI API key
- Sentence Transformers
- ChromaDB
- Pandas, NumPy, Matplotlib
- Jupyter Lab

## Data

The notebooks use a collection of academic papers (GPT-1 through GPT-4) as source documents for the RAG system. The evaluation dataset is generated synthetically using these papers.

## Next Steps

After completing these notebooks, consider:
- Implementing more sophisticated retrieval strategies like hybrid search or multi-query retrieval
- Exploring different query reformulation techniques based on domain knowledge
- Integrating with a production system for real-world testing and refinement
# Systematically Improve Your AI Agents

A collection of systematic approaches to building, evaluating, and improving AI agents. This repository contains practical cookbooks that guide you through the process of creating robust AI agents and systematically measuring and improving their performance.

## Overview

Building effective AI agents requires more than just connecting to the latest LLM API. This repository provides structured approaches to developing agents that are reliable, efficient, and continuously improving. Each cookbook in this collection focuses on a specific agent type and walks through a methodical process for:

1. **Establishing evaluation frameworks** - Creating robust datasets and metrics to measure performance
2. **Implementing agent architectures** - Building modular, configurable agent components
3. **Systematic improvement** - Using data-driven approaches to enhance agent capabilities
4. **Performance visualization** - Tracking improvements and identifying bottlenecks

## Cookbooks

### [RAG Agent](/agents/rag_agent)
A systematic approach to building and improving Retrieval-Augmented Generation (RAG) agents. This cookbook guides you through creating evaluation datasets, implementing RAG agents with adaptive retrieval strategies, and systematically measuring and improving their performance.

### [Coming Soon] Function Calling Agent
A methodical approach to building agents that can effectively use function calling capabilities to interact with external tools and APIs.

### [Coming Soon] Multi-Agent Systems
Techniques for building and orchestrating systems of multiple specialized agents that can collaborate to solve complex tasks.

### [Coming Soon] Planning Agent
Approaches to implementing agents with sophisticated planning capabilities that can break down complex tasks into manageable steps.

## Common Structure

Each agent cookbook follows a consistent structure to facilitate learning and comparison:

1. **Data Engineering** - Creating evaluation datasets and establishing metrics
2. **Agent Implementation** - Building the agent architecture and evaluation framework

## Getting Started

To get started with any cookbook:

1. Clone this repository
```bash
git clone https://github.com/langwatch/cookbooks.git
cd cookbooks
```

2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Navigate to the specific agent directory and follow the instructions in its README

## Contributing

Contributions are welcome! If you have ideas for new agent cookbooks or improvements to existing ones, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Kasparro Multi-Agent Content Generation System

Overview

This repository implements a LangChain-based multi-agent system that converts structured product data into fully JSON-formatted content outputs, including a product page, FAQ page, and product comparison page.

The solution is designed to demonstrate the use of an established agentic framework rather than custom orchestration logic. It follows best practices for agent boundaries, tool usage, and model-driven generation.

Architecture

The system is built using LangChain and is composed of multiple agents, each with a clearly defined responsibility:

Parse Agent
Normalizes raw product JSON into a structured internal representation.

Question Generation Agent
Generates informational, usage, and safety-related questions using the language model.

Template Agent
Produces structured content using prompt-based templates for product pages and FAQ items.

Comparison Agent
Compares two products and generates structured comparison output.

Assembler Agent
Combines all intermediate outputs into a final unified JSON object.

All agents are implemented using LangChain tool abstractions and are orchestrated through LangChain’s agent execution flow.

Key Features

LangChain-based agent orchestration
Clear separation of agent responsibilities
Model-driven content generation
Reusable prompt templates
Fully JSON-structured outputs
Extensible and maintainable design

API Key Configuration

Do not hard-code API keys in the notebook or source code.

Before running the system, configure one of the following environment variables:

OPENAI_API_KEY
or
GEMINI_API_KEY

API keys may also be stored in a local file such as /content/OPENAI_API_KEY and loaded securely at runtime.

Execution Notes

The system is implemented using LangChain’s agent and tool abstractions as required.

In environments with limited API quota or inactive billing, execution may fail with rate limit or quota errors. The architecture and implementation remain valid and will run successfully when provided with a valid API key and sufficient quota.

Output

The final output is a single JSON object containing:

Product page content
FAQ page with multiple FAQ items
Product comparison data

The JSON output can be saved to disk and downloaded for further use.

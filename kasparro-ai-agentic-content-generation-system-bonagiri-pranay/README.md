Kasparro – Multi-Agent Content Generation System

Assignment: Applied AI / Agentic Content System
Author: Bonagiri Pranay

 Overview

This project implements a modular, rule-based, multi-agent AI system that generates structured content pages for a skincare product.
It follows the specifications outlined in the Kasparro Applied AI Assignment PDF.

The system produces 3 content pages:

Product Page

FAQ Page

Comparison Page

All pages are generated using reusable content blocks, specialized agents, and a central Orchestrator.

Project Architecture
kasparro-ai-agentic-content-generation-system-bonagiri-pranay/
│
├── src/
│   ├── core/
│   │   ├── models.py
│   │   ├── orchestrator.py
│   │
│   ├── agents/
│   │   ├── product_parser_agent.py
│   │   ├── question_generation_agent.py
│   │   ├── faq_page_agent.py
│   │   ├── product_page_agent.py
│   │   ├── comparison_page_agent.py
│   │
│   ├── blocks/
│   │   ├── content_blocks.py
│   │
│   ├── data/
│   │   ├── product_input.json
│   │
│   ├── output/
│   │   ├── faq.json
│   │   ├── product_page.json
│   │   ├── comparison_page.json
│   │
│   └── templates/
│
└── docs/
    ├── projectdocumentation.md

 System Flow
1️ ProductParserAgent

Parses the input JSON and constructs a structured Product object.

2️ QuestionGenerationAgent

Generates 15 pre-defined questions across 5 categories:

Informational

Usage

Safety

Purchase

Comparison

3️ FAQPageAgent

Builds the FAQ page using:

Questions list

Rule-based answer generator (content_blocks.answer_question)

4️ ProductPageAgent

Creates structured product content divided into sections:

Benefits

Ingredients

Usage

Safety

Pricing

5️ ComparisonPageAgent

Compares the input product with a hard-coded competitor and produces:

Ingredient comparison

Benefit comparison

Price comparison

6️ Orchestrator

Runs all agents in sequence and writes structured JSON output.

 Generated Output Files (JSON)

Located in:

src/output/


Files:

faq.json

product_page.json

comparison_page.json

These JSON files follow clean, export-ready structures suitable for downstream use.

 Content Blocks

All reusable logic (benefits, ingredients, safety, pricing, FAQ answers) is implemented in:

src/blocks/content_blocks.py


This ensures:

Clean architecture

Easy extensibility

Reusable components for future agentic systems

 Running the System

Inside the src/ directory:

python -m core.orchestrator


Outputs will appear automatically in:

src/output/

 What This System Demonstrates

Modular multi-agent orchestration

Clean architecture with reusable blocks

Structured JSON generation

Rule-based NLP answering using only given product data

Real-world simulation of agentic content pipelines

 Author

Bonagiri Pranay
Applied AI Track – Kasparro Internship Assignment
Email: bonagiripranay123@gmail.com

 


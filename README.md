# Devscale Bootcamp Assignment #1

## Assignment #1
- Bikin simple chatbot - input ()
    - Context Injection
- Pipeline -> 3 steps process to achieve something.
    - Generate_raw_information(topic)
    - Summarize(raw_information)
    - Extract(summarized_content)

## Overview

This repository contains Assignment #1 for the Devscale Bootcamp. It includes two Python projects:

- `01_SIMPLE_CHATBOT`: a simple conversational chatbot using OpenAI's Chat Completions API, configured as a Bali travel agent.
- `02_PIPELINE`: a small prompt-response pipeline demonstrating raw response generation, summarization, and structured response parsing.

There is also a `main.py` file that serves as a minimal placeholder entrypoint for the repository.

## Repository Structure

- `main.py` - Simple entrypoint script that prints a greeting.
- `pyproject.toml` - Project metadata and dependency declaration.
- `01_SIMPLE_CHATBOT/chatbot.py` - Chatbot implementation using OpenAI and environment-based API key loading.
- `01_SIMPLE_CHATBOT/context.py` - Travel information context used by the chatbot to answer questions.
- `02_PIPELINE/function.py` - Functions for generating raw responses, summarizing text, and generating structured responses with OpenAI.
- `02_PIPELINE/models.py` - `pydantic` data model for structured responses.
- `README.md` - This file.

## Requirements

- Python 3.11 or newer
- OpenAI Python SDK
- python-dotenv
- pydantic

## Setup

1. Clone or copy the repository to your local machine.
2. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install openai python-dotenv pydantic
```

4. Create a `.env` file in the repository root with your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Run the simple chatbot

Navigate to `01_SIMPLE_CHATBOT` and run:

```bash
cd 01_SIMPLE_CHATBOT
python chatbot.py
```

The chatbot uses the `INFORMATION_CONTEXT` defined in `context.py` and interacts with the OpenAI API using a system prompt designed for a Bali travel agent.

### Run the pipeline demo

Navigate to `02_PIPELINE` and run:

```bash
cd 02_PIPELINE
python pipeline.py
```

Then provide a recipe-related prompt when asked. The script will print:

- a raw model response
- a summarized response
- a structured response parsed into the `Recipee` model

## Notes

- `chatbot.py` is designed for interactive use and keeps conversation history across turns.
- `function.py` uses `openai.chat.completions.create` and `openai.chat.completions.parse` for structured output.
- If you want to run package-style with `pyproject.toml`, you can also install the project in editable mode:

```bash
python -m pip install -e .
```

---

Assignment #1 showcases basic prompt engineering, environment configuration, and simple OpenAI-powered chat and response pipeline logic.
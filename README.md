# llm-fine-tuning-prepare-dataset-from-md

This repository contains Python scripts that help in preparing blog posts written in Markdown (`mdx`) format for fine-tuning a Large Language Model (LLM). The scripts clean the blog posts, generate applicable `instruction` prompts for each using Ollama, and convert the prompts and blog posts into an Alpaca-formatted JSON file suitable for training.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Scripts Overview](#scripts-overview)
  - [clean_blog_posts.py](#clean_blog_postspy)
  - [md_to_alpaca.py](#md_to_alpacapy)

---

### Prerequisites

Ensure you have Python installed on your system. Additionally, ensure [Ollama](https://ollama.com/) is installed and running and the [Ollama Python SDK](https://github.com/ollama/ollama-python) is installed:

---

### Scripts Overview

#### clean_blog_posts.py

**Purpose:**  
This script reads blog posts in `mdx` format and cleans them by removing unnecessary elements and saves them in `md` format to be used by the `md_to_alpaca.py` script.

**Usage:**

1. Place your `mdx` files in the `data` directory.
2. Run the script from the command line:

   ```bash
   python clean_blog_posts.py
   ```

3. The cleaned blog posts will be saved in the `cleaned-data` directory or an output directory.

**Details:**  
- **Input:** Markdown files (`mdx`).
- **Output:** Cleaned markdown files (`md`).

#### md_to_alpaca.py

**Purpose:**  
Generates `instruction` prompts from the cleaned markdown blog posts using Ollama and convert the prompts and blog posts into an Alpaca-formatted JSON file, which can be used to fine-tune an LLM.

**Usage:**

1. Ensure you have the cleaned markdown files from in the `cleaned-data` directory and that Ollama is running.
2. Run the script from the command line:

   ```bash
   python md_to_alpaca.py
   ```

3. The Alpaca-formatted JSON file will be generated.

**Details:**  
- **Input:** Cleaned markdown files.
- **Output:** Alpaca-formatted JSON file (`data.json`).

# Cookiecutter Hardware Test Report

A Cookiecutter template for quickly generating a hardware test report project structure. This template scaffolds:

- **Markdown-based** sections for introduction, results, and conclusion
- A **report/** folder for combined outputs (Markdown and PDFs)
- **Tools** (e.g., `generate-pdf.py`) to compile Markdown into a PDF using [Pandoc](https://pandoc.org/) and the [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) LaTeX template (optionally via Docker)

## Features

- **Automatic Project Structure**: Creates folders and files for a typical hardware test report (intro, results, conclusion).  
- **Pre-filled Cookiecutter Prompts**: (e.g., project name, author, timestamp, intended audience).  
- **Markdown to PDF**: Includes a Python script (`tools/generate-pdf.py`) that compiles your report into a professional-looking PDF.  
- **Docker or Local Installation**: Choose between running Pandoc locally or using the [Docker-based pandoc/extra image](https://github.com/pandoc/dockerfiles).

## Getting Started

### 1. Install Cookiecutter

If you haven’t installed Cookiecutter yet:

```fish
pip install cookiecutter
```

### 2. Generate Your Project
```fish
cookiecutter https://github.com/rasmusravn/cookiecutter-hardware-test-report.git
```

Cookiecutter Prompts

You will be asked for:

    project_name: e.g., “QCP Self-Heating Test”
    project_slug: automatically derived from project_name (e.g., qcp_self_heating_test)
    author: your name
    intro: short description/introduction
    purpose: purpose/goal of the hardware test
    intended_audience: who the report is for (e.g., “Engineering, QA, Management”)

Cookiecutter will then create a new folder named after your project_slug with the following structure:

```bash

your_project_slug/
├── 1-intro.md
├── 2-results.md
├── 3-conclusion.md
├── images/
├── report/
└── tools/
    ├── generate-email.py
    ├── generate-pdf.py
    ├── __init__.py
    └── package-project.py
```

### 3. Fill In Your Report

Open and edit the Markdown files:

    1-intro.md
    2-results.md
    3-conclusion.md

You can add additional sections, images, or test data as needed. Place images in the images/ folder and reference them in your Markdown using standard Markdown syntax:

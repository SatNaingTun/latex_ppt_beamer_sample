# LaTeX and PDF Conversion Tools

This repository contains scripts to convert LaTeX beamer presentations to PowerPoint and various utilities to convert PDF documents to editable PowerPoint (`.pptx`) or Word (`.docx`) formats.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Virtual Environment](#setup-virtual-environment)
- [Installation](#installation)
- [Usage](#usage)
  - [PDF to PowerPoint](#pdf-to-powerpoint)
  - [PDF to Word](#pdf-to-word)
<!-- - [Git Setup](#git-setup) -->

---

## Prerequisites
Before starting, ensure you have the following installed:
* [Python](https://www.python.org/) (Version 3.8 or higher)
* [Git](https://git-scm.com/)

---

## Setup Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

### Windows (PowerShell/CMD)
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### MacOS or Linux
```
python3 -m venv .venv
source .venv/bin/activate
```

## Installation
```
pip install -r requirements.txt
```

## Usage
### Pdf to PowerPoint
```
python convert2pptx.py presentation.pdf presentation.pptx
```
or
```
python pdf2ppt.py presentation.pdf presentation.pptx
```

### Pdf to Word
```
python3 convert2docx.py presentation.pdf presentation.docx
```
# LaTeX and PDF Conversion Tools

This repository contains scripts to convert LaTeX beamer presentations to PowerPoint and various utilities to convert PDF documents to editable PowerPoint (`.pptx`) or Word (`.docx`) formats.

## Table of Contents
- [Prerequisites](#prerequisites)
  -[LaTeX Setup for VS Code](#latex-setup-for-vs-code)
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


## LaTeX Setup for VS Code
To edit and compile LaTeX documents within VS Code, follow these steps:

1.  **Install a LaTeX Distribution**:
    * **Windows**: [MiKTeX](https://miktex.org/download)
    * **macOS**: [MacTeX](https://www.tug.org/mactex/)
    * **Linux**: [TeX Live](https://www.tug.org/texlive/)
2.  **Install VS Code Extension**: Search for and install **LaTeX Workshop** in the Extensions marketplace (`Ctrl+Shift+X`).
3.  **Perl Installation**: Some packages require Perl.
    * **Windows**: Download and install [Strawberry Perl](https://strawberryperl.com/).
    * **macOS/Linux**: Pre-installed, or install via package manager (`brew install perl` or `sudo apt install perl`).
4.  **Verify Installation**: Open a `.tex` file and press `Ctrl+Alt+B` (Windows/Linux) or `Cmd+Option+B` (macOS) to build the PDF.

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
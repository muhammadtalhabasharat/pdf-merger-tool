# PDF Merger

A Python CLI tool that automatically finds every PDF file in the current folder and merges them into a single `merged.pdf`, in alphabetical order.

## Features
- Auto-detects all `.pdf` files in the directory (no need to list filenames manually)
- Skips its own previous output (`merged.pdf`) so it's safe to re-run
- Skips unreadable/corrupted files individually instead of crashing the whole merge

## Tech used
Python 3, [`pypdf`](https://pypi.org/project/pypdf/) — the actively maintained successor to PyPDF2

## How to run
```bash
pip install -r requirements.txt
python pdf_merger.py
```
Place the script in the same folder as the PDFs you want to merge, then run it. The result is saved as `merged.pdf` in that same folder.

## Example
```
Found 3 PDF file(s) to merge.
Added: chapter1.pdf
Added: chapter2.pdf
Added: chapter3.pdf
Successfully merged all files into 'merged.pdf'!
```# pdf-merger-tool
A Python CLI tool that automatically finds and merges every PDF in a directory into one file, with per-file error handling.

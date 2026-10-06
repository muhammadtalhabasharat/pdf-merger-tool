"""
PDF Merger
Automatically finds every PDF file in the current directory (excluding its
own previous output) and merges them into a single file, in alphabetical order.
"""

import os
from pypdf import PdfWriter


def find_pdf_files(directory="."):
    files = [f for f in os.listdir(directory) if f.endswith(".pdf") and f != "merged.pdf"]
    files.sort()
    return files


def merge_pdfs(pdf_files, output_name="merged.pdf"):
    writer = PdfWriter()

    for filename in pdf_files:
        try:
            with open(filename, "rb") as pdf_file:
                writer.append(pdf_file)
            print(f"Added: {filename}")
        except Exception as e:
            print(f"Skipped {filename} (could not read it: {e})")

    writer.write(output_name)
    writer.close()


def main():
    pdf_files = find_pdf_files()

    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    print(f"Found {len(pdf_files)} PDF file(s) to merge.")
    merge_pdfs(pdf_files)
    print("Successfully merged all files into 'merged.pdf'!")


if __name__ == "__main__":
    main()

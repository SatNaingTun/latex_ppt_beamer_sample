import sys
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    print(f"Converting {pdf_file} to {docx_file}...")
    cv = Converter(pdf_file)
    cv.convert(docx_file) # All pages by default
    cv.close()
    print("Conversion complete!")

if __name__ == "__main__":
    # Check if we have enough arguments (script name + input + output)
    if len(sys.argv) < 3:
        print("Usage: python convert.py <input_pdf_path> <output_docx_path>")
    else:
        pdf_path = sys.argv[1]
        docx_path = sys.argv[2]
        convert_pdf_to_docx(pdf_path, docx_path)
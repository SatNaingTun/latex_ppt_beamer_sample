import sys
import pdf2pptx

def convert_pdf_to_ppt(pdf_file, pptx_file):
    print(f"Converting {pdf_file} to {pptx_file}...")
    try:
        # Pass the missing arguments:
        # resolution=300 (standard), start_page=0, page_count=None (all pages)
        pdf2pptx.convert_pdf2pptx(
            pdf_file, 
            pptx_file,
            resolution=300,
            start_page=0,
            page_count=None
        )
        print("Conversion complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf2ppt.py <input_pdf_path> <output_pptx_path>")
    else:
        pdf_path = sys.argv[1]
        ppt_path = sys.argv[2]
        convert_pdf_to_ppt(pdf_path, ppt_path)
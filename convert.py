import os
from docx2pdf import convert

def convert_docx_to_pdf(docx_path, pdf_output_path):
    try:
        convert(docx_path, pdf_output_path)
        print(f"File {docx_path} convertito in {pdf_output_path}")
    except Exception as e:
        print(f"Errore durante la conversione: {e}")

def main():
    docx_folder = "CV/"
    pdf_folder = "CV/"

    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    for filename in os.listdir(docx_folder):
        if filename.endswith(".docx"):
            docx_path = os.path.join(docx_folder, filename)
            pdf_filename = os.path.splitext(filename)[0] + "_.pdf"
            pdf_output_path = os.path.join(pdf_folder, pdf_filename)

            convert_docx_to_pdf(docx_path, pdf_output_path)

if __name__ == "__main__":
    main()

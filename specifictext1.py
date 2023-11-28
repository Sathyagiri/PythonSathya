import PyPDF2

def extract_text_from_pdf_pypdf2(pdf_path):
    text = ""

    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

# Example usage:
pdf_path = r"C:\Users\satvijay2\Downloads\Sarun MT_Nov_2021.htm.pdf"
extracted_text = extract_text_from_pdf_pypdf2(pdf_path)

print(extracted_text)

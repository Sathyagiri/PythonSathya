import re
import PyPDF2

def extract_specific_text(pdf_path, target_text):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Use a regular expression to find the specific text
            match = re.search(target_text, text)

            if match:
                print(f"Found '{target_text}' on Page {page_num + 1}")

# Example usage
pdf_path = r"C:\Users\satvijay2\Downloads\Sarun MT_Nov_2021.htm.pdf"  # Replace with your PDF file path
target_text = 'From'  # Replace with the text you're looking for
extract_specific_text(pdf_path, target_text)
print(extract_specific_text)


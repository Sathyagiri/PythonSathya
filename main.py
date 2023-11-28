import os
import PyPDF2

def split_pdf(input_pdf_path, output_folder):

    with open(input_pdf_path, 'rb') as file:

        pdf_reader = PyPDF2.PdfReader(file)


        os.makedirs(output_folder, exist_ok=True)


        for page_num in range(len(pdf_reader.pages)):

            pdf_writer = PyPDF2.PdfWriter()


            pdf_writer.add_page(pdf_reader.pages[page_num])


            output_pdf_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")


            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"Page {page_num + 1} saved to {output_pdf_path}")


input_pdf_path = r'C:\Users\satvijay2\Downloads\Sarun MT_Nov_2021.htm.pdf'  # Replace with your input PDF file path
output_folder = r'C:\Users\satvijay2\Downloads\output1.pdf'  # Replace with your desired output folder

split_pdf(input_pdf_path, output_folder)




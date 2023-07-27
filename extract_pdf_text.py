"""
from PyPDF2 import PdfReader
reader = PdfReader("example.pdf")
nop = len(reader.pages)
page = reader.pages[0]

text = page.extract_text()
print(text)
reader.close()

"""
import PyPDF2

# A Function used to read pdf files. 

def extractor(file_path):
    try:
        #open pdffile
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file) #assign a variable to the file handler
            num_pages = len(pdf_reader.pages) #find the number of pages in the pdf

            # iterate through each page in the pdf and assign it to a "text" variable. 
            text = ""
            for page_num in range(num_pages): 
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            return text
    # Error handling 
    except FileNotFoundError:
        print("File not found.")
    except PyPDF2._utils.PdfStreamError:
        print("Unable to read the PDF file.")



# Testing read_pdf
if __name__ == "__main__":
    pdf_file_path = r"C:\Users\besky\OneDrive\Desktop\CP317 Project\example.pdf"
    pdf_content = extractor(pdf_file_path)
    print(pdf_content)

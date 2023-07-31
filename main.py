from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pdf_extractor import PDFExtractor
from ppt_creator import PPTCreator

def extract_and_convert(pdf_path):
    pdf_extractor = PDFExtractor(pdf_path)
    text_content = pdf_extractor.extract_text()
    image_files = pdf_extractor.extract_images()

    ppt_path = asksaveasfilename(defaultextension=".pptx", filetypes=[("PowerPoint", "*.pptx")])
    if not ppt_path:
        return  # User cancelled the dialog

    ppt_creator = PPTCreator(ppt_path)
    ppt_creator.create_ppt(text_content, image_files)

def main():
    root = Tk()
    root.withdraw()  # Hide the main window

    messagebox.showinfo("PDF to PPT Converter", "Select a PDF file to convert to PowerPoint.")

    pdf_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not pdf_path:
        return  # User cancelled the dialog

    try:
        extract_and_convert(pdf_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Success", "The PPT file was created successfully.")

    root.mainloop()

if __name__ == "__main__":
    main()

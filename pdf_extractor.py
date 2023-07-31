import pdfplumber
from PIL import Image, UnidentifiedImageError
import io


class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            text_content = [page.extract_text().replace(".", ". ") for page in pdf.pages]
        return text_content

    def extract_images(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            images = []
            for page in pdf.pages:
                for img in page.images:
                    try:
                        image_data = img["stream"].get_data()
                        image = Image.open(io.BytesIO(image_data))
                        images.append(image)
                    except UnidentifiedImageError:
                        print("An image in the PDF could not be identified by PIL and was skipped.")
            return images



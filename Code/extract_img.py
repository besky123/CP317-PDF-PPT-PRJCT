import os
import PyPDF2
from PIL import Image
import io
from io import BytesIO
from reportlab.lib.utils import ImageReader 


def img_extract(save_directory):
    pdf_file = open(r"C:\Users\besky\OneDrive\Desktop\CP317 Project\png.pdf", 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)

    #Create directory, if one doesn't exist 
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for i in range(0, len(read_pdf.pages)):
        page = read_pdf.pages[i]
        xObject = page['/Resources']['/XObject'].get_object()
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                stream = xObject[obj].get_object()
                data = stream.get_data()

                """
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"
                img = Image.open(data)
                imagename = "image" + str(i) + "_" + str(obj[1:]) + ".png"
                full_path = os.path.join(save_directory, imagename)
                img.save(full_path)
                """

                """
                # Check if the image data is valid before attempting to open it
                if data[:4] == b'\x89PNG' or (data[0] == b'\xff' and data[1] == b'\xd8'):
                    img = Image.open(io.BytesIO(data))
                    imagename = "image" + str(i) + "_" + str(obj[1:]) + ".png"
                    full_path = os.path.join(save_directory, imagename)
                    img.save(full_path)
                else:
                    print(f"Skipping invalid image data on page {i + 1}, object {obj}.")
                """
                try:
                    img = Image.open(io.BytesIO(data))
                    imagename = "image" + str(i) + "_" + str(obj[1:]) + ".png"
                    full_path = os.path.join(save_directory, imagename)
                    img.save(full_path)
                except:
                    print(f"Skipping invalid image data on page {i + 1}, object {obj}.")
                    continue
    pdf_file.close()


#Test
save_ = "/Users/besky/OneDrive/Desktop/CP317 Project/images/exctacted_images"
img_extract(save_)

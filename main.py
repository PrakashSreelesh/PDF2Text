from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def pdffile_convert(name):
    PDF_file = name
    pages = convert_from_path(PDF_file, 500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    image_counter = 1

    for page in pages:
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG')
        image_counter += 1
    print(type(pages))
    filelimit = image_counter - 1
    outfile = PDF_file.replace('.pdf', '.txt')
    with open(outfile, "w") as f:
        for i in range(1, filelimit + 1):
            filename = "page_" + str(i) + ".jpg"
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            text = str(((pytesseract.image_to_string(Image.open(filename)))))
            text = text.replace('-\n', '')
            f.write(text)

    return outfile
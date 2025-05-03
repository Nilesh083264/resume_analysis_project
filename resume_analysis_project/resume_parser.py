import pytesseract
from PIL import Image
import docx
import PyPDF2
import re


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([para.text for para in doc.paragraphs])

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        text = extract_text_from_image(file_path)
    else:
        return "", False

    gap = detect_education_gap(text)
    return text, gap

def detect_education_gap(text):
    years = list(map(int, re.findall(r'(20\d{2}|19\d{2})', text)))
    years = sorted(set(years))
    for i in range(1, len(years)):
        if years[i] - years[i-1] > 2:
            return True
    return False


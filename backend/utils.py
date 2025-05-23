import pdfplumber

def extract_text(file, manual_text):
    if file and file.filename.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file and file.filename.endswith('.txt'):
        return file.read().decode('utf-8')
    elif manual_text:
        return manual_text
    return ""
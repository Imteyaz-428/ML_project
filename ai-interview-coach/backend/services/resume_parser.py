import fitz


def extract_resume_text(file_path: str):
    pdf = fitz.open(file_path)
    
    text = ""
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text
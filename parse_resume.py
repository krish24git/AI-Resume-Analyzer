from pdfminer.high_level import extract_text
import os

def parse_resume(file_storage):
    # Save temporarily
    temp_path = os.path.join("uploads", file_storage.filename)
    file_storage.save(temp_path)

    # Extract text from PDF
    text = extract_text(temp_path)

    # Clean up
    os.remove(temp_path)

    return text

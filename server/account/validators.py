import os


def validate_file_extension(value):
    ext = os.path.splitext(value)[1]  # [1] returns path+filename
    valid_extensions = [".pdf", ".doc", ".docx"]
    if ext.lower() not in valid_extensions:
        return False
    return True

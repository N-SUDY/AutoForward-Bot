import random
import string
import hashlib

def generate_random_string(length=10):
    """Generate a random string of alphanumeric characters."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def get_hashed_filename(filename):
    """Generate a unique hashed filename based on the original filename."""
    file_extension = filename.split('.')[-1]
    unique_suffix = generate_random_string()
    hashed_filename = hashlib.sha256(
        (filename + unique_suffix).encode('utf-8')).hexdigest()
    return f"{hashed_filename}.{file_extension}"

def is_valid_extension(filename, allowed_extensions):
    """Check if the file extension is in the allowed extensions list."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def is_valid_size(file_size, max_size_bytes):
    """Check if the file size is within the allowed maximum size."""
    return file_size <= max_size_bytes

def is_valid_text(message_text, keywords):
    """Check if the message text contains any of the specified keywords."""
    return any(keyword in message_text for keyword in keywords)
    
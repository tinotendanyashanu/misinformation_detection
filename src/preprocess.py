def preprocess_text(text):
    """Cleans and preprocesses the input text."""
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    # Remove extra spaces
    text = ' '.join(text.split())
    return text

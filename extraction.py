import pdfplumber


def extract_text(uploaded_file):
    """Extracts text from the uploaded PDF using pdfplumber, adding markers for headings based on font size."""
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            extracted_text = (
                page.extract_text()
            )  # Fallback in case word-level extraction fails

            # Extract words with formatting info
            words = page.extract_words(extra_attrs=["size", "fontname"])

            for word_data in words:
                word = word_data["text"]
                font_size = word_data.get(
                    "size", 10
                )  # Default to 10 if size is missing
                font_name = word_data.get("fontname", "").lower()

                # Determine if text is a heading based on font size or bold style
                if font_size > 14 and "bold" in font_name:
                    text += f"## {word} ## "  # Wrap headings with ##
                else:
                    text += word + " "

            # If word-level extraction fails, use extracted_text as a backup
            if not words and extracted_text:
                text += extracted_text + "\n"

    return text

import re

import name_extractor as a

from .. import \
    logger  # Import the logger from the parent package's __init__.py


def extract_names_from_text(input_str):
    """Extract names from a text file or direct input."""
    logger.debug("enter extract_names_from_text.")
    print(a.PACKAGE_NAME)
    # If input is a file, read content
    try:
        with open(input_str, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        text = input_str  # Assume input is direct text

    # Basic regex for capitalized words (Assumes names are capitalized)
    names = re.findall(r"\b[A-Z][a-z]+\b", text)
    return names

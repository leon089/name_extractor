"""test.

This module provides a simple command-line interface (CLI) for extracting names
from input arguments.
It expects at least one argument and raises an error if none are provided.
"""

import argparse
import sys

from name_extractor.json.converter import extract_names_from_json
from name_extractor.text.converter import extract_names_from_text


def main():
    """
    Entry point for the CLI.

    This module provides a simple command-line interface (CLI) for extracting
    names from input arguments.
    It expects at least one argument and raises an error if none are provided.
    """
    parser = argparse.ArgumentParser(
        description="Extract names from text or JSON"
    )

    parser.add_argument("input", help="Input file path or text string")
    parser.add_argument(
        "--json", action="store_true", help="Specify if input is a JSON file"
    )

    args = parser.parse_args()

    if args.json:
        try:
            names = extract_names_from_json(args.input)
        except FileNotFoundError:
            print(f"Error: File '{args.input}' not found.", file=sys.stderr)
            sys.exit(1)
    else:
        try:
            names = extract_names_from_text(args.input)
        except FileNotFoundError:
            print(f"Error: File '{args.input}' not found.", file=sys.stderr)
            sys.exit(1)

    print("\nExtracted Names:", ", ".join(names))


if __name__ == "__main__":
    main()

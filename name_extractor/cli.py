"""asjdh.

This module provides a simple command-line interface (CLI) for extracting names
from input arguments.
It expects at least one argument and raises an error if none are provided.
"""

import sys


def main():
    """
    Entry point for the CLI.

    This function retrieves command-line arguments (excluding the script name),
    checks if any arguments are provided, and prints a message indicating the
    source of name extraction.

    Raises:
        ValueError: If no command-line arguments are provided.
    """
    args = sys.argv[1:]  # Get CLI arguments
    if len(args) == 0:
        raise ValueError("No arguments provided.")
    print(f"Extracting names from: {args}")


if __name__ == "__main__":
    main()

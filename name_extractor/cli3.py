"""asjdh.

This module provides a simple command-line interface (CLI) for extracting names
from input arguments.
It expects at least one argument and raises an error if none are provided.
"""

# name_extractor/cli.py
import click

from name_extractor.json.converter import extract_names_from_json
from name_extractor.text.converter import extract_names_from_text


@click.command()
@click.argument("input")
@click.option(
    "--json",
    "is_json",
    is_flag=True,
    help="Specify if the input is a JSON file",
)
def main(input, is_json):
    """etz.

    test
    Extract names from TEXT or JSON files.
    """
    try:
        if is_json:
            names = extract_names_from_json(input)
        else:
            names = extract_names_from_text(input)
    except FileNotFoundError:
        click.secho(f"Error: File '{input}' not found.", fg="red", err=True)
        raise click.ClickException(f"File '{input}' not found.")

    click.echo(f"Extracted Names: {', '.join(names)}")


if __name__ == "__main__":
    main()

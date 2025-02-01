# tests/test_cli.py
import sys
# Mocking the functions to isolate CLI logic
from unittest.mock import patch

import pytest

from name_extractor.cli2 import main


def test_extract_names_from_text_success(monkeypatch, capsys):
    # Simulate command-line arguments
    monkeypatch.setattr(
        sys, "argv", ["cli2.py", "sample2.txt"]
    )  # "sample2.txt" will not be evaluated!

    # Mocking extract_names_from_text
    # package.sub_package.module.method
    # with patch("name_extractor.text.converter.extract_names_from_text", return_value=["Alice", "Bob"]):
    # You need to patch it relative to where it’s used, not where it’s defined:
    with patch(
        "name_extractor.cli2.extract_names_from_text", return_value=["Alice", "Bob"]
    ):
        main()

        main()

    captured = capsys.readouterr()
    print("captured.out:", captured.out)
    assert "Extracted Names: Alice, Bob" in captured.out


def test_extract_names_from_json_success(monkeypatch, capsys):
    # Simulate command-line arguments with --json flag
    monkeypatch.setattr(
        sys, "argv", ["XXX", "sample.json", "--json"]
    )  # argv[0] will not be evaluated in test!

    # Mocking extract_names_from_json
    with patch(
        "name_extractor.cli2.extract_names_from_json", return_value=["Charlie", "David"]
    ):
        main()

    captured = capsys.readouterr()
    assert "Extracted Names: Charlie, David" in captured.out


def test_file_not_found_text(monkeypatch, capsys):
    # Simulate command-line arguments for a missing text file
    monkeypatch.setattr(sys, "argv", ["cli2.py", "missing.txt"])

    # Mock extract_names_from_text to raise FileNotFoundError
    with patch(
        "name_extractor.cli2.extract_names_from_text", side_effect=FileNotFoundError
    ):
        with pytest.raises(SystemExit) as excinfo:
            main()

    captured = capsys.readouterr()
    assert "Error: File 'missing.txt' not found." in captured.err
    assert excinfo.value.code == 1


def test_file_not_found_json(monkeypatch, capsys):
    # Simulate command-line arguments for a missing JSON file
    monkeypatch.setattr(sys, "argv", ["cli2.py", "missing.json", "--json"])

    # Mock extract_names_from_json to raise FileNotFoundError
    with patch(
        "name_extractor.cli2.extract_names_from_json", side_effect=FileNotFoundError
    ):
        with pytest.raises(SystemExit) as excinfo:  # prog ends with SystemExit
            main()

    captured = capsys.readouterr()
    assert "Error: File 'missing.json' not found." in captured.err
    assert excinfo.value.code == 1


def test_missing_input_argument(monkeypatch):
    # Simulate missing input argument
    monkeypatch.setattr(sys, "argv", ["cli2.py"])

    # Expect argparse to exit with code 2 due to missing required argument
    with pytest.raises(SystemExit) as excinfo:
        main()

    assert excinfo.value.code == 2

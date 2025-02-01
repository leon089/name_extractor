# tests/test_cli.py
import sys, pytest
from io import StringIO
from name_extractor.cli import main

# The capsys fixture is a built-in fixture provided by pytest. 
# It allows you to capture output that is written to stdout and stderr during test execution.
def test_main_ok(monkeypatch, capsys):
    # Simulate command-line arguments
    test_args = ["cli.py", "sample.txt"]
    monkeypatch.setattr(sys, "argv", test_args)
    
    # Run the CLI main function
    main()

    # Capture printed output
    captured = capsys.readouterr()

    # Assert the expected output
    assert "Extracting names from: ['sample.txt']" in captured.out

def test_main_bad(monkeypatch, capsys):
    # Simulate command-line arguments
    test_args = ["cli.py"]
    monkeypatch.setattr(sys, "argv", test_args)

    # Check for ValueError when no arguments are provided
    with pytest.raises(ValueError, match="No arguments provided."):
        main()
"""asjdh.

This module provides a simple command-line interface (CLI) for extracting names
from input arguments.
It expects at least one argument and raises an error if none are provided.
"""

# __init__.py
import logging

PACKAGE_NAME = "MyPackage"
DEBUG_MODE = True

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # levels DEBUG, INFO, WARNING, ERROR, or CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Get a logger for the package
logger = logging.getLogger(__name__)

# Example of logging different messages
logger.debug("Debug message - This is useful for diagnosing problems.")
logger.info(
    "Info message - This provides general information about the package behavior."
)
logger.warning(
    "Warning message - Something is not quite right, but the package is still working."
)
logger.error("Error message - Something went wrong.")
logger.critical("Critical message - A serious problem occurred.")

# If you are doing initialization or other work, you can log those events too.
logger.info("Initializing the package...")

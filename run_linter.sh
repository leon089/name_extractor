#!/bin/bash

# Linting Script
# This script runs Black, Flake8, Mypy, and isort on the source code.

# Source directory (adjust if needed)
SRC_DIR="name_extractor"

echo "🚀 Starting Linting Process..."

# Run Black
echo "🔍 Running Black..."
poetry run black $SRC_DIR --exclude '(venv|\.venv|site-packages)' || exit 1

# Run Flake8
echo "🐍 Running Flake8..."
poetry run flake8 $SRC_DIR --exclude=venv,.venv,site-packages || exit 1

# Run Mypy
echo "🧠 Running Mypy..."
poetry run mypy $SRC_DIR --exclude '(venv|\.venv|site-packages)' || exit 1

# Run isort
echo "📦 Running isort..."
poetry run isort $SRC_DIR --skip venv --skip .venv --skip site-packages || exit 1

echo "✅ All linters passed successfully!"

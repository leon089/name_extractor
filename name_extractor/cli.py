import sys

def main():
    args = sys.argv[1:]  # Get CLI arguments
    if len(args) == 0:
        raise ValueError("No arguments provided.")
    print(f"Extracting names from: {args}")

if __name__ == "__main__":
    main()

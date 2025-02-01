import json


def extract_names_from_json(file_path):
    """Extract names from JSON file assuming it has a 'names' key."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict) and "names" in data:
        return data["names"]
    elif isinstance(data, list):  # Assume list of dictionaries with 'name' key
        return [item.get("name", "") for item in data if "name" in item]

    return []

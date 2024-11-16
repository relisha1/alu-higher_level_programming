#!/usr/bin/python3
"""
Script that adds all command-line arguments to a list and saves them to a JSON file.
If the file `add_item.json` exists, the list is loaded from the file and updated.
If the file doesn't exist, an empty list is created and the arguments are added to it.
"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items():
    """
    Adds command-line arguments to a list and saves the list in a JSON file.
    If the file exists, it loads the current list; if not, it starts with an empty list.
    The arguments are appended to the list, and the updated list is saved back to the file.
    """
    try:
        # Try to load the existing list from the file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        items = []

    # Append all command-line arguments (except the script name itself)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_items()


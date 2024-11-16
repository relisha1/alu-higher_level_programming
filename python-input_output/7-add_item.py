#!/usr/bin/python3
"""
Script that adds all command-line arguments to a list and saves them to a JSON file.
It uses `save_to_json_file` to save the list and `load_from_json_file` to load it.
If the file doesn't exist, it is created.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items():
    """
    Add command-line arguments to a list and save the list in a JSON file.
    If the file exists, the current list is loaded; otherwise, an empty list is used.
    Arguments are added to the list, and the updated list is saved back to the file.
    """
    try:
        # Try to load the existing list from the file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        items = []

    # Add all command-line arguments (except the script name itself)
    items.extend(sys.argv[1:])
    
    # Save the updated list back to the file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_items()


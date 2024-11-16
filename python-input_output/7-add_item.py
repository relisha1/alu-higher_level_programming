#!/usr/bin/python3
"""
This script adds command-line arguments to a list and saves the list to a JSON file.

The script performs the following tasks:
- If the file 'add_item.json' exists, the script loads the list stored in the file.
- If the file doesn't exist, the script creates a new file with an empty list.
- It appends the command-line arguments passed to the script (excluding the script name) to the list.
- Finally, the updated list is saved back to 'add_item.json'.

Usage:
    The script expects command-line arguments to be passed when executed.
    For example:
        ./7-add_item.py argument1 argument2 argument3

    If run multiple times, the script will continue to add new arguments to the list stored in the file.
    The file is created if it doesn't already exist, and the list is updated accordingly.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items():
    """
    Adds command-line arguments to a list and saves the list in a JSON file.
    
    This function does the following:
    1. Tries to load the existing list from the 'add_item.json' file.
    2. If the file does not exist, it initializes an empty list.
    3. Appends all command-line arguments (except the script name) to the list.
    4. Saves the updated list back to the file 'add_item.json'.
    """
    try:
        # Try to load the existing list from the file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        items = []

    # Append all command-line arguments (excluding the script name itself)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_items()


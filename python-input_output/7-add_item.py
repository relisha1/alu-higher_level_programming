#!/usr/bin/python3
import sys
import os

# Importing required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# File to store the JSON data
filename = "add_item.json"

# Check if the file exists
if os.path.exists(filename):
    # Load the existing list from the file
    items = load_from_json_file(filename)
else:
    # Initialize an empty list if the file does not exist
    items = []

# Add command-line arguments (excluding the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)


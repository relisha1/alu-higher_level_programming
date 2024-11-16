#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Define the filename
filename = 'add_item.json'

# Try to load the current list from the file, or start with an empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all arguments (from sys.argv[1:] to the list)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)


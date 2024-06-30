# file_reader.py

import os

def read_prompts(folder_path):
    # Initialize an empty dictionary
    file_contents = {}

    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Add the content to the dictionary with the short file name as the key
            short_name = os.path.splitext(filename)[0]
            file_contents[short_name] = content
    
    return file_contents

import os
import json

def load_entities(data_folder):
    """
    Load texts from all .txt files in the specified folder into a dictionary.
    
    Args:
    data_folder (str): The path to the folder containing the .txt files.
    
    Returns:
    dict: A dictionary where the keys are filenames (without extension) and the values are the contents of the files.
    """
    texts_dict = {}

    # Loop through each file in the data folder
    for filename in os.listdir(data_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(data_folder, filename)
            # Read the content of the file and add it to the dictionary
            with open(file_path, 'r', encoding='utf-8') as file:
                key = os.path.splitext(filename)[0]
                texts_dict[key] = file.read()

    return texts_dict

# Example usage within the same script (optional)
if __name__ == "__main__":
    data_folder = 'path_to_data_folder'
    texts_dict = load_entities(data_folder)
    for key, text in texts_dict.items():
        print(f"{key}: {text}")

    # Save the dictionary to a JSON file if needed
    with open('texts_dict.json', 'w', encoding='utf-8') as json_file:
        json.dump(texts_dict, json_file, ensure_ascii=False, indent=4)

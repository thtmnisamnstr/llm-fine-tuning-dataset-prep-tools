import os
import json

def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def convert_md_files_to_alpaca_format(source_directory, output_file):
    alpaca_data = []

    # Iterate through all files in the source directory
    for filename in os.listdir(source_directory):
        if filename.endswith('.md'):
            file_path = os.path.join(source_directory, filename)
            md_content = read_md_file(file_path)

            # Create a dictionary entry for each MD file
            alpaca_entry = {
                "instruction": "",
                "input": "",
                "output": md_content.strip()
            }

            # Append the entry to the list
            alpaca_data.append(alpaca_entry)

    # Write the list of dictionaries to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(alpaca_data, json_file, indent=4, ensure_ascii=False)

# Define the source directory and output file
source_directory = './cleaned-data'
output_file = './data.json'

# Convert MD files to Alpaca-formatted JSON
convert_md_files_to_alpaca_format(source_directory, output_file)

print(f"Alpaca-formatted JSON has been saved to {output_file}")
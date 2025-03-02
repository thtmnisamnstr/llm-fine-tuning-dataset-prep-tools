import os
import json
import ollama

def read_md_file(file_path):
    """
    Read the content of a markdown file.
    
    Args:
        file_path (str): The path to the markdown file.
        
    Returns:
        str: The content of the markdown file.
    """
    # Open the file in read mode with UTF-8 encoding and return its contents.
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_instruction(prompt):
    """
    Generate an LLM prompt using Ollama API that would produce the given response.
    
    Args:
        prompt (str): The content of the markdown file to be used as the response.
        
    Returns:
        str: The generated LLM prompt.
    """
    # Create a client instance for the Ollama API, specifying the host address.
    client = ollama.Client(host='http://127.0.0.1:11434')
    
    # Define the Ollama Generate model, prompt, and stream parameters.
    ollama_model = 'qwen2.5:32b'
    ollama_prompt = (f'Write a fairly simple LLM prompt that includes key points, tone, '
                     f'and any necessary context that would generate the given response. '
                     f'I only want the prompt text value with no preamble and no summarization or recap of the given response.\nResponse:\n{prompt}')
    ollama_stream = False
    
    # Generate the response using Ollama and extract the 'response' field.
    ollama_response = client.generate(model=ollama_model, prompt=ollama_prompt, stream=ollama_stream)['response']
    
    # Return the generated instruction.
    return ollama_response

def convert_md_files_to_alpaca_format(source_directory, output_file):
    """
    Convert markdown files in a directory to an Alpaca-formatted JSON file suitable for LLM fine-tuning.
    
    Args:
        source_directory (str): The path to the directory containing markdown files.
        output_file (str): The path where the Alpaca-formatted JSON file will be saved.
    """
    alpaca_data = []  # Initialize an empty list to store data in Alpaca format.

     # Count the total number of .md files in the source directory.
    total_files = len([f for f in os.listdir(source_directory) if f.endswith('.md')])
    
    # Iterate through each file markdown in the source directory.
    for file_count, filename in enumerate(os.listdir(source_directory), start=1):
        if filename.endswith('.md'):
            file_path = os.path.join(source_directory, filename)
            
            # Read the content of the markdown file.
            md_content = read_md_file(file_path)
            
            # Print progress information for each file being processed.
            print(f"Processing file {file_count} of {total_files}: {filename}")
            
            # Generate an instruction using the Ollama API based on the markdown content.
            instruction = generate_instruction(md_content)
            
            if instruction is None:
                continue
            
            # Create a dictionary entry for the current file in Alpaca format.
            alpaca_entry = {
                "instruction": instruction,
                "input": "",
                "output": md_content.strip()
            }
            
            # Append the dictionary entry to the list of Alpaca data.
            alpaca_data.append(alpaca_entry)
    
    # Write the list of Alpaca data to a JSON file with pretty-printing and UTF-8 encoding.
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(alpaca_data, json_file, indent=4, ensure_ascii=False)

# Define the source directory containing markdown files and the output file path.
source_directory = 'cleaned-data'
output_file = 'data.json'

# Call the function to convert markdown files to Alpaca-formatted JSON.
convert_md_files_to_alpaca_format(source_directory, output_file)

# Print a confirmation message indicating where the Alpaca-formatted JSON file is saved.
print(f"Alpaca-formatted JSON has been saved to {output_file}")
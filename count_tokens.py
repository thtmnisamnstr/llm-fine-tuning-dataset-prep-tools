import json
import tiktoken

def count_tokens(text, model="gpt-3.5-turbo"):
    """
    Count the number of tokens in a given text using the specified OpenAI model.
    
    Args:
        text (str): The input text for which to count tokens.
        model (str): The name of the OpenAI model to use for tokenization. Default is "gpt-3.5-turbo".
        
    Returns:
        int: The number of tokens in the input text.
    """
    # Load the tokenizer for the specified model
    encoding = tiktoken.encoding_for_model(model)
    
    # Encode the text and return the length of the token list
    num_tokens = len(encoding.encode(text))
    return num_tokens

def read_alpaca_json(file_path):
    """
    Read the Alpaca-formatted JSON file.
    
    Args:
        file_path (str): The path to the Alpaca-formatted JSON file.
        
    Returns:
        list: A list of dictionaries containing 'instruction', 'input', and 'output'.
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def print_token_counts(alpaca_data):
    """
    Print the number of tokens in each entry's combined 'instruction' and 'output'.
    
    Args:
        alpaca_data (list): A list of dictionaries containing 'instruction', 'input', and 'output'.
    """
    for index, entry in enumerate(alpaca_data, start=1):
        # Combine 'instruction' and 'input'
        combined_text = f"{entry['instruction']}\n{entry['output']}"
        
        # Count tokens
        token_count = count_tokens(combined_text)
        
        # Print the token count
        print(f"Entry {index}: {token_count} tokens. {entry['instruction'][:50]}")

if __name__ == "__main__":
    """
    Main entry point of the script. Reads Alpaca-formatted JSON and print token counts.
    """
    input_file = 'data.json'  # The Alpaca-formatted JSON file from the previous program

    # Read the Alpaca-formatted JSON data
    alpaca_data = read_alpaca_json(input_file)
    
    # Print token counts for each entry
    print_token_counts(alpaca_data)

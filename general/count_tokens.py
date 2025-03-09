import json
import tiktoken
import argparse

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

def print_token_counts(alpaca_data, max_tokens):
    """
    Print the number of tokens in each entry's combined 'instruction' and 'output'.
    If token count exceeds max_tokens, print a warning.
    Args:
        alpaca_data (list): A list of dictionaries containing 'instruction', 'input', and 'output'.
        max_tokens (int): The maximum allowed token count for an entry.
    """
    for index, entry in enumerate(alpaca_data, start=1):
        # Combine 'instruction' and 'input'
        combined_text = f"{entry['instruction']}\n{entry['input']}\n{entry['output']}"

        # Count tokens
        token_count = count_tokens(combined_text)

        # Print the entry number and token count
        print(f"Entry {index}: {token_count} tokens. {entry['instruction'][:50]}")

        # Print a warning if the entry exceeds max_tokens
        if token_count > max_tokens:
            print(f"\033[93mWarning: Exceeds {max_tokens} tokens.\033[0m")

if __name__ == "__main__":
    """
    Main entry point of the script. Reads Alpaca-formatted JSON and prints token counts.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Count tokens in Alpaca-formatted JSON data.")
    parser.add_argument('filename', type=str, help='Path to the Alpaca-formatted JSON file.')
    parser.add_argument('max_tokens', type=int, help='Maximum allowed token count for an entry.')

    # Parse arguments
    args = parser.parse_args()

    input_file = args.filename
    max_tokens = args.max_tokens

    try:
        # Read the Alpaca-formatted JSON data
        alpaca_data = read_alpaca_json(input_file)
        # Print token counts for each entry
        print_token_counts(alpaca_data, max_tokens)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

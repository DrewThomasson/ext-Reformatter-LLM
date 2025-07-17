import argparse
import ollama
import nltk
from nltk.tokenize import sent_tokenize
from tqdm import tqdm

DEFAULT_PROMPT = (
    "Reformat the following sentence for proper quote usage. "
    "Output only the reformatted sentence, and nothing else.\n"
    "{sentence}"
)

def download_nltk_data():
    try:
        sent_tokenize("test")  # Attempt to use the tokenizer to check if it's available
    except LookupError:
        print("Downloading NLTK 'punkt' tokenizer...")
        nltk.download('punkt')

def install_model(model_name):
    print(f"Model '{model_name}' not found.")
    confirm = input("Do you want to try pulling it? (y/n): ")
    if confirm.lower() == 'y':
        try:
            ollama.pull(model=model_name)
            print("Model pulled successfully.")
        except Exception as e:
            print(f"Error pulling model: {e}")
            exit(1)
    else:
        print("Operation cancelled.")
        exit()

def check_model(model_name):
    try:
        models = ollama.list()
        # Check if the model exists in the list of available models
        if hasattr(models, 'models'):
            available_models = [model.name for model in models.models]
            return model_name in available_models
        elif isinstance(models, dict) and 'models' in models:
            available_models = [model['name'] for model in models['models']]
            return model_name in available_models
        return False
    except Exception as e:
        print(f"Error checking models: {e}")
        return False

def format_quotes_in_text(model_name, text_content, output_file, prompt_template):
    download_nltk_data()  # Ensure NLTK data is available
    sentences = sent_tokenize(text_content)
    formatted_text = []

    # Using tqdm to show progress
    for sentence in tqdm(sentences, desc="Formatting Sentences"):
        prompt = prompt_template.format(sentence=sentence)
        try:
            response = ollama.generate(model=model_name, prompt=prompt)
            
            # Handle different response formats - try multiple ways to extract the response
            response_text = None
            
            # Method 1: Try accessing as attribute
            if hasattr(response, 'response'):
                response_text = response.response
            # Method 2: Try accessing as dictionary
            elif isinstance(response, dict) and 'response' in response:
                response_text = response['response']
            # Method 3: Try accessing message content (some versions)
            elif isinstance(response, dict) and 'message' in response and 'content' in response['message']:
                response_text = response['message']['content']
            # Method 4: If it's a string directly
            elif isinstance(response, str):
                response_text = response
            
            if response_text:
                formatted_text.append(response_text.strip())
            else:
                print(f"Could not extract response from: {type(response)}")
                formatted_text.append(sentence)  # Fallback to the original sentence
                
        except Exception as e:
            print(f"Error generating response for sentence: {sentence[:50]}... Error: {e}")
            formatted_text.append(sentence)  # Fallback to the original sentence

    # Write each sentence on a new line for better readability
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(formatted_text))
    print(f"Formatted text saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Format quotes in text using Ollama LLM.\n"
            "You can provide a custom prompt template with --prompt. The default is:\n"
            f"    {DEFAULT_PROMPT.replace('{sentence}', '[sentence]')}\n"
            "Use '{sentence}' in your prompt to substitute the target sentence."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--modelname", "-m", "-model", required=True, help="Name of the Ollama model.")
    parser.add_argument("--textfile_input", "--input", "-in", required=True, help="Path to the input text file.")
    parser.add_argument("-o", "--output", "-out", default="output.txt", help="Optional output file name.")
    parser.add_argument(
        "--prompt",
        help=(
            "Custom prompt template to use for each sentence. "
            "Use '{sentence}' where the input sentence should be inserted. "
            "If not provided, defaults to:\n"
            f"{DEFAULT_PROMPT.replace('{sentence}', '[sentence]')}"
        ),
        default=DEFAULT_PROMPT
    )

    args = parser.parse_args()

    if not check_model(args.modelname):
        install_model(args.modelname)

    try:
        with open(args.textfile_input, 'r', encoding='utf-8') as file:
            text_content = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{args.textfile_input}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        exit(1)

    format_quotes_in_text(args.modelname, text_content, args.output, args.prompt)

if __name__ == "__main__":
    main()
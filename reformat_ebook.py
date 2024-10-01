import argparse
import ollama
import nltk
from nltk.tokenize import sent_tokenize
from tqdm import tqdm

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
        ollama.pull(model=model_name)
        print("Model pulled successfully.")
    else:
        print("Operation cancelled.")
        exit()

def check_model(model_name):
    try:
        ollama.list()  # Adjusted to use list, which presumably shows available models
        return True
    except Exception as e:
        return False

def format_quotes_in_text(model_name, text_content, output_file):
    download_nltk_data()  # Ensure NLTK data is available
    sentences = sent_tokenize(text_content)
    formatted_text = []

    # Using tqdm to show progress
    for sentence in tqdm(sentences, desc="Formatting Sentences"):
        response = ollama.generate(model=model_name, prompt=sentence)
        if 'message' in response and 'content' in response['message']:
            formatted_text.append(response['message']['content'].strip())
        else:
            print("Unexpected response format:", response)
            formatted_text.append(sentence)  # Fallback to the original sentence

    with open(output_file, 'w') as file:
        file.write(' '.join(formatted_text))
    print(f"Formatted text saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Format quotes in text using Ollama LLM.")
    parser.add_argument("--modelname", "-m", "-model", required=True, help="Name of the Ollama model.")
    parser.add_argument("--textfile_input", "--input", "-in", required=True, help="Path to the input text file.")
    parser.add_argument("-o", "--output","-out", default="output.txt", help="Optional output file name.")
    
    args = parser.parse_args()

    if not check_model(args.modelname):
        install_model(args.modelname)

    with open(args.textfile_input, 'r') as file:
        text_content = file.read()

    format_quotes_in_text(args.modelname, text_content, args.output)

if __name__ == "__main__":
    main()

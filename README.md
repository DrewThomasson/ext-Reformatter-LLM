# ext-Reformatter-LLM
Reformat texts using LLM's and Ollama- (Will later change to use llama cpp pip instead to make it easier on everyone)


# 📚 Text-Reformatter-LLM 📚

A Python app that leverages **Ollama LLM** to format lines in your ebook, making sure quotes are used correctly and the text is polished, perfect for further processing with **BookNLP**. 

## Features
- Automatically formats ebook quotes for cleaner text.
- Uses Ollama for LLM useage
- Outputs formatted text in a new file.

## 🚀 Quick Start Guide

### 1. Requirements
- Python 3.12.4 (Tested version, should work with other versions)
- **Ollama** from [Ollama.com](https://ollama.com) (Not just the pip package, also the local Ollama install)
- `nltk` for tokenizing sentences
- `tqdm` for progress tracking

### 2. Install Instructions

#### Step 1: Install Python dependencies
First, ensure Python 3.12.4 is installed on your machine. Then, install the required Python packages:

```bash
pip install ollama nltk tqdm
```

#### Step 2: Install Ollama
Visit [Ollama](https://ollama.com) and follow the instructions to install the **Ollama** application locally on your machine.

#### Step 4: Clone the Repository and Run the App

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/Text-Reformatter-LLM.git
cd Text-Reformatter-LLM
```

2. Run the app:

```bash
python reformat_ebook.py --modelname MODEL_NAME --input INPUT_FILE.txt -o OUTPUT_FILE.txt
```

### 3. Example Usage

```bash
python reformat_ebook.py --modelname llm-english --input story.txt -o formatted_story.txt
```

### ⚙️ Arguments
- `--modelname` / `-m`: The name of the Ollama model to use.
- `--input` / `-in`: Path to the input text file.
- `--output` / `-o`: Optional output file name (defaults to `output.txt`).
- `--prompt`: *(Optional)* Custom prompt template for the model. Use `{sentence}` in your prompt template to substitute each sentence from your input file.  
  If not provided, the default prompt is:  
  ```
  Reformat the following sentence for proper quote usage. Output only the reformatted sentence, and nothing else.
  {sentence}
  ```

### Help Command 

You can view all available command-line options and see the default prompt by running:
```bash
usage: reformat_ebook.py [-h] --modelname MODELNAME --textfile_input TEXTFILE_INPUT [-o OUTPUT] [--prompt PROMPT]

Format quotes in text using Ollama LLM.
You can provide a custom prompt template with --prompt. The default is:
    Reformat the following sentence for proper quote usage. Output only the reformatted sentence, and nothing else.
    [sentence]
Use '{sentence}' in your prompt to substitute the target sentence.

optional arguments:
  -h, --help            show this help message and exit
  --modelname MODELNAME, -m MODELNAME, -model MODELNAME
                        Name of the Ollama model.
  --textfile_input TEXTFILE_INPUT, --input TEXTFILE_INPUT, -in TEXTFILE_INPUT
                        Path to the input text file.
  -o OUTPUT, --output OUTPUT, -out OUTPUT
                        Optional output file name.
  --prompt PROMPT       Custom prompt template to use for each sentence. Use '{sentence}' where the input sentence should be inserted. If not provided, defaults to:
                        Reformat the following sentence for proper quote usage. Output only the reformatted sentence, and nothing else.
                        [sentence]
```


### 4. Customization
By default, the script ensures that the quotes in the input text are formatted correctly by prompting the LLM for each sentence.  
**Customization:**  
- To change the model's behavior, use `--prompt` with your own instruction string, for example:
  ```bash
  python reformat_ebook.py --modelname llm-english --input story.txt --output formatted_story.txt --prompt "Correct grammar and punctuation for the following sentence. Output only the corrected sentence:\n{sentence}"
  ```
- The placeholder `{sentence}` will be replaced with each sentence from your input file.

### 🔧 Troubleshooting
- If the model isn't installed, the app will prompt you to pull it using Ollama.
- If you encounter any issues, ensure that **Ollama** is correctly installed and running locally.

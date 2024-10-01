# ext-Reformatter-LLM
Reformat texts using LLM's and Ollama


# 📚 Text-Reformatter-LLM 📚

A Python app that leverages **Ollama LLM** to format lines in your ebook, making sure quotes are used correctly and the text is polished, perfect for further processing with **BookNLP**. 

## 🌟 Features
- Automatically formats ebook quotes for cleaner text.
- Seamlessly integrates with **Ollama** for powerful natural language generation.
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

#### Step 3: Download NLTK data
The app uses NLTK's `punkt` tokenizer. It will automatically prompt you to download the necessary data if it’s not available.

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

This command reads the file `story.txt`, reformats the text using the **llm-english** model, and outputs the formatted version into `formatted_story.txt`.

### ⚙️ Arguments
- `--modelname` / `-m`: The name of the Ollama model to use.
- `--input` / `-in`: Path to the input text file.
- `--output` / `-o`: Optional output file name (defaults to `output.txt`).

### 4. Customization
The default behavior ensures that the quotes in the input text are formatted correctly. You can further tweak the prompt in the `reformat_ebook.py` to adjust the formatting style or add additional model logic.

### 🌐 Dependencies
- **Ollama**: Install from [Ollama](https://ollama.com).
- **nltk**: Natural Language Toolkit for sentence tokenization.
- **tqdm**: For showing progress during text processing.

### 🔧 Troubleshooting
- If the model isn't installed, the app will prompt you to pull it using Ollama.
- If you encounter any issues, ensure that **Ollama** is correctly installed and running locally.

Enjoy a well-formatted, quote-perfect ebook! 📖✨

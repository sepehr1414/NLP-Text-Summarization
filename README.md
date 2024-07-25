# NLP Text Summarization Project

## Description
This project implements an advanced extractive text summarization system using Natural Language Processing (NLP) techniques. The primary objective is to generate concise, informative summaries of large texts while preserving the most crucial information. This tool is particularly valuable for condensing lengthy documents, research papers, or articles into more manageable summaries, all while adhering to a specified context window limit.
Key Features:

1. Extractive Summarization: The system employs an extractive approach, which involves selecting and arranging the most important sentences from the original text to form a coherent summary. This method ensures that the summary retains the original wording and style of the source material.
2. Multi-Document Handling: The project can process multiple input documents simultaneously. It's designed to handle two types of texts: the main input text and a style text. This feature allows for potential applications in style transfer or comparative summarization.
3. Adaptive Summarization: The system dynamically adjusts its summarization process based on a configurable context window limit. This adaptability ensures that the final output always fits within the specified token limit, making it suitable for various applications with different length constraints.
4. Proportional Document Handling: When dealing with multiple input documents, the system calculates target lengths for each document proportionally. This ensures that each document is represented fairly in the final summary, based on its original length and the overall context window limit.
5. Iterative Summarization: For exceptionally long inputs, the system employs an iterative approach. It first summarizes sections of the text, then summarizes these summaries, repeating the process until the desired length is achieved. This method allows for effective handling of very large documents.

## Technical Details:

Tokenization: The system uses NLTK's tokenization tools to break down the input text into sentences and words. This granular approach allows for precise analysis and selection of content.
- Frequency Analysis: A key part of the summarization process involves calculating word frequencies. The system identifies the most frequent and thus potentially most important words in the text, excluding common stopwords.
- Sentence Scoring: Based on the word frequencies, each sentence in the document is assigned a score. This score represents the sentence's importance in the context of the entire document.
- Summary Generation: The system selects the highest-scoring sentences to form the summary. The number of sentences selected is dynamically adjusted to fit within the context window limit.
- Context Window Management: The project includes sophisticated logic to manage the context window, ensuring that the final output never exceeds the specified token limit. This is crucial for applications where there are strict limits on output length, such as in certain AI models or text processing systems.
## How It Works

1. The system first tokenizes the input texts and calculates their lengths.
2. It then computes target lengths for each document proportionally to fit within the context window limit.
3. If the input texts exceed the context window limit, the system slices the documents and summarizes each slice.
4. The summarization process involves:
   - Calculating word frequencies
   - Scoring sentences based on word frequencies
   - Selecting top-scoring sentences to form the summary
5. The process is repeated until the final summary fits within the context window limit.

## How to Run

To run this project, follow these steps:

1. Ensure you have Python installed on your system.

2. Install the required dependencies:
   ```
   pip install nltk
   ```

3. Place all the project files (`config.py`, `extractive_summarization.py`, and `main.py`) in the same directory.

4. Run the main script:
   ```
   python main.py
   ```

5. The script will output the final summarized text that fits within the specified context window limit.

Note: On the first run, the script may download necessary NLTK data. Ensure you have an active internet connection for this step.

## Requirements

- Python 3.x
- NLTK library


# Step 0: Imports
# You will need:
# - json (to read JSONL)
# - re (for cleaning text)
# - collections (optional for counting)


# Step 1: Define STOP WORDS
# Create a small set of common words like:
# "the", "is", "and", "of", "to", etc.
# Keep it simple (10–30 words)


STOP_WORDS = {
    # add words here
}


# Step 2: Text Cleaning Function
def clean_text(text):
    """
    Input: raw string (title + abstract)
    Output: cleaned string

    Steps:
    1. Convert to lowercase
    2. Remove punctuation (use regex)
    3. Remove extra spaces
    """
    # TODO: implement
    return text


# Step 3: Tokenization Function
def tokenize(text):
    """
    Input: cleaned text
    Output: list of words

    Steps:
    1. Split by space
    2. Remove empty tokens
    """
    # TODO: implement
    return []


# Step 4: Remove Stop Words
def remove_stopwords(tokens):
    """
    Input: list of tokens
    Output: filtered tokens

    Remove words that are in STOP_WORDS
    """
    # TODO: implement
    return []


# Step 5: Count Token Frequency
def get_token_freq(tokens):
    """
    Input: list of tokens
    Output: dictionary {word: count}

    Example:
    ["search", "engine", "search"] -> {"search": 2, "engine": 1}
    """
    # TODO: implement
    return {}


# Step 6: Process ONE document
def process_document(doc):
    """
    Input: one JSON object (paper)
    Output: processed document

    Steps:
    1. Extract:
        - id
        - title
        - abstract
    2. Combine title + abstract
    3. Clean text
    4. Tokenize
    5. Remove stopwords
    6. Count frequency

    Output format:
    {
        "id": ...,
        "tokens": {word: count}
    }
    """
    # TODO: implement
    return {}


# Step 7: Read JSONL file
def load_documents(file_path, limit=1000):
    """
    Input: file path
    Output: list of processed documents

    Steps:
    1. Open file
    2. Read line by line (VERY IMPORTANT)
    3. Convert each line to JSON
    4. Process document
    5. Stop after 'limit' documents
    """
    documents = []

    # TODO: implement

    return documents


# Step 8: Main function
def main():
    file_path = "cs_ir_papers.jsonl"  # update path if needed

    docs = load_documents(file_path, limit=1000)

    # Print sample output
    print(docs[0])

    # Optional:
    # - print number of documents
    # - print some stats


if __name__ == "__main__":
    main()
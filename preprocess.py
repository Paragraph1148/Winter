import json # for jsonl
import re # for cleaning text
import collections # for counting

STOP_WORDS = {
    "and",
    "but",
    "or",
    "nor",
    "for",
    "yet",
    "so",
    "about",
    "above",
    "across",
    "after",
    "against",
    "along",
    "among",
    "around",
    "at",
    "before",
    "behind",
    "below",
    "beneath",
    "beside",
    "between",
    "beyond",
    "by",
    "despite",
    "down",
    "during",
    "except",
    "from",
    "in",
    "inside",
    "into",
    "like",
    "near",
    "of",
    "off",
    "on",
    "onto",
    "out",
    "over",
    "past",
    "since",
    "through",
    "throughout",
    "to",
    "toward",
    "under",
    "underneath",
    "until",
    "up",
    "upon",
    "with",
    "within",
    "without",
    "i",
    "me",
    "my",
    "myself",
    "we",
    "us",
    "our",
    "ourselves",
    "you",
    "your",
    "yours",
    "yourself",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "her",
    "hers",
    "herself",
    "it",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "being",
    "been",
    "have",
    "has",
    "had",
    "do",
    "does",
    "did",
    "will",
    "would",
    "shall",
    "should",
    "may",
    "might",
    "must",
    "can",
    "could"
}


def clean_text(text):
    """
    Input: raw string (title + abstract)
    Output: cleaned string

    Steps:
    1. Convert to lowercase
    2. Remove punctuation (use regex)
    3. Remove extra spaces
    """
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", text.lower())).strip()


def tokenize(text):
    """
    Input: cleaned text
    Output: list of words

    Steps:
    1. Split by space
    2. Remove empty tokens
    """
    return [token for token in text.split(' ') if token]


def remove_stopwords(tokens):
    """
    Input: list of tokens
    Output: filtered tokens

    Remove words that are in STOP_WORDS
    """
    return [word for word in tokens if word not in STOP_WORDS]


def get_token_freq(tokens):
    """
    Input: list of tokens
    Output: dictionary {word: count}

    Example:
    ["search", "engine", "search"] -> {"search": 2, "engine": 1}
    """
    return dict(Counter(tokens))


def process_document(page):
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
    # 1 get fields
    pid = page.get("id")
    ptit = page.get("title")
    pabs = page.get("abstract")

    # 2 combine text and abstract
    combined = f"{ptit} {pabs}"

    # 3 clean
    cleaned = clean_text(combined)

    # 4 tokenize
    tokens = tokenize(cleaned)

    # 5 remove stopwords
    tokens = remove_stopwords(tokens)

    # 6 count freq
    freq = get_token_freq(tokens)
    
    return {"id": pid, "tokens": freq}


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
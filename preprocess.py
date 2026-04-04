import json # for jsonl
import re # for cleaning text
from collections import Counter # for counting

STOP_WORDS = {
    "a",
    "an",
    "the",
    "this",
    "that",
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
    1. Replace hyphen with whitespace
    2. Remove punctuation (use regex)
    3. Filter out tokens with length of characters < 2
    """
    text = re.sub(r"(?<=[A-Za-z])-(?=[A-Za-z])", " ", text) # replace hyphen with whitespace
    cleaned = re.sub(
        r"\s+",                     # collapse multiple whitespaces
        " ", 
        re.sub(
            r"[^\w\s]", "",         # remove punctuation
            text.lower())).strip()  # lowercase and trim ends
    long_tokens = [tok for tok in cleaned.split(" ") if len(tok) > 2]
    return " ".join(long_tokens)    # re-join the string

def remove_urls(text):
    # Matches http(s)://… or www.… until a whitespace character
    url_pattern = r"https?://\S+|www\.\S+"
    return re.sub(url_pattern, "", text)

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
    removedurl = remove_urls(combined)
    cleaned = clean_text(removedurl)

    # 4 tokenize
    tokens = tokenize(cleaned)

    # 5 remove stopwords
    tokens = remove_stopwords(tokens)

    # 6 count freq
    freq = get_token_freq(tokens)

    # 7 track document length
    char_len = len(cleaned)
    token_len = len(tokens)

    return {"id": pid, "tokens": freq, "char_len": char_len, "token_len": token_len}


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
    total_chars = 0
    total_tokens = 0

    with open(file_path, mode="r", encoding="utf-8") as f: # with guarantees file is closed after block ends, even if error
        for line_no, line in enumerate(f, start=1):
            if len(documents) >= limit:     # stop after reaching limit
                break

            line = line.strip()
            if not line:                    # skip blank lines
                continue

            try:
                paper = json.loads(line)    # convert line to dict
            except json.JSONDecodeError as exc:
                print(f"Line {line_no}: JSON decode error:- {exc}")
                continue
            
            doc = process_document(paper)
            documents.append(doc)

            total_chars  += doc["char_len"]
            total_tokens += doc["token_len"]
            
    avg_chars  = total_chars / len(documents) if documents else 0
    avg_tokens = total_tokens / len(documents) if documents else 0
    print(f"Average characters per doc: {avg_chars:.1f}")
    print(f"Average tokens per doc:    {avg_tokens:.1f}")

    total_docs = len(docs)
    print(f"Total documents loaded: {total_docs}")

    vocab = set()
    for doc in docs:
        vocab.update(doc["tokens"].keys())

    print(f"Vocabulary size (unique tokens): {len(vocab)}")

    return documents


def main():
    file_path = "cs_ir_papers.jsonl"  # update path if needed
    docs = load_documents(file_path, limit=1000)

    # Print sample output
    # print(docs[0])

    # Optional:
    # - print number of documents
    # - print some stats
    # if docs:
    #     # Show the first processed document as a sanity check
    #     print("First document:", docs[0])
    #     print(f"Total documents loaded: {len(docs)}")
    # else:
    #     print("No valid documents were found.")


if __name__ == "__main__":
    main()
from index import tokenizer

def tokenize_query(query: str) -> list:
    """Tokenize the query and return tokens in a list"""

    # This list holds tokens inside
    tokens = []

    for word in query.split(' '):
        word = tokenizer(word)
        tokens.append(word)
    
    return tokens
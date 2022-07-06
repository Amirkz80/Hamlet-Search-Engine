import math
from index import tokenizer
from boolean_operators import bool_search

def tokenize_query(query: str) -> list:
    """Tokenize the query and return tokens in a list"""

    # This list holds tokens inside
    tokens = []

    for word in query.split(' '):
        word = tokenizer(word)
        # Word cann't be None
        if word:
            tokens.append(word)
    
    return tokens


def tf_idf_calculator(term_frequency: int) -> float:
    """Calculates the TF-IDF score of the given document and returns it"""

    tf = math.log10(1 + term_frequency)
    return tf    


def ranker(tokens: list) -> list:
    """Gets tokens, ranks the docs that contain tokens and
    returns list of relative docs that are sorted by TF-IDF """

    # This dictionary contains doc_ids and their TF-IDF score
    doc_scores = {}
    # final sorted by score docs
    final_docs = []

    for token in tokens:
        # Docs that contain the token
        token_info = bool_search(token)

        for doc_id in token_info.keys():
            if doc_id not in doc_scores.keys():
                doc_scores[doc_id] = tf_idf_calculator(token_info[doc_id])
            else:
                doc_scores[doc_id] += tf_idf_calculator(token_info[doc_id])
    
    for pair in sorted(doc_scores.items(), key=lambda item: item[1]):
        final_docs.append(pair[0])
    
    return final_docs
import math
import os
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


def tf_idf_calculator(raw_term_frequency: int, docs_with_token_length: int) -> float:
    """Calculates the TF-IDF score of the given document and returns it"""

    # Number of ALL docs in repo
    N = len(os.listdir('repo/'))

    tf = math.log10(1 + raw_term_frequency)
    idf = math.log10(N/(docs_with_token_length + 1))

    tf_idf = tf * idf
    return tf_idf    


def ranker(tokens: list) -> list:
    """Gets tokens, ranks the docs that contain tokens and
    returns list of relative docs that are sorted by TF-IDF """

    # This dictionary contains doc_ids and their TF-IDF score
    doc_scores = {}
    # final sorted by score docs
    final_docs = []

    for token in tokens:
        # The dictionary that contains term frequnecy of the word
        token_info = bool_search(token)
        # Number of all tokens that contain token
        docs_with_token_num = len(token_info.keys())

        # Iterate over all docs that contain the token
        # They are in token term_frequncy dict (are the keys basically)
        for doc_id in token_info.keys():
            if doc_id not in doc_scores.keys():
                doc_scores[doc_id] = tf_idf_calculator(token_info[doc_id], docs_with_token_num)
            else:
                doc_scores[doc_id] += tf_idf_calculator(token_info[doc_id], docs_with_token_num)
    
    for pair in sorted(doc_scores.items(), key=lambda item: item[1]):
        final_docs.append(pair[0])
    
    # We reverse the list to have descending order
    # This function modifies list directly
    final_docs.reverse()

    return final_docs
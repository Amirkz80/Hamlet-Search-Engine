import math
import os
from datetime import datetime
from index import tokenizer
from boolean.boolean_operators import bool_search
from heapq import nlargest

def chunk(number: int, chunks_number: int):
    """Gets range of numbers and returns start and end number
    of each divided group, all groups are equal in members number,
    EXCEPT LAST ONE if number has a DEVIDE REMAINING"""
    chunks = []
    remaining = number % chunks_number
    gp_members_num = int(number / chunks_number)
    i = 1

    for chunk_number in range(1, chunks_number + 1):
        if chunk_number != chunks_number:
            chunks.append([i, i + (gp_members_num - 1)])
            i += gp_members_num
        else:
            chunks.append([i, i + (gp_members_num - 1 + remaining)])

    return chunks

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

def tf_idf_calculator(raw_term_frequency: int, idf: float) -> float:
    """Calculates the TF-IDF score of the given document and returns it"""

    return math.log10(1 + raw_term_frequency) * idf    

def ranker(doc_scores: dict, length: int, token_info: dict) -> list:
    """ranks the docs that contain token and returns list of
    relative docs that are sorted by TF-IDF """


    idf = math.log10(len(os.listdir('repo/'))/(length + 1))
    
    # doc_scores dictionary contains doc_ids and their TF-IDF score
    # Iterate over all docs that contain the token
    # They are in token term_frequncy dict (are the keys basically)    
    for doc_id in token_info:
        if doc_id not in doc_scores:
            doc_scores[doc_id] = tf_idf_calculator(token_info[doc_id], idf)
        else:
            doc_scores[doc_id] += tf_idf_calculator(token_info[doc_id], idf)

    return doc_scores

def rank_tokens(tokens: list) -> list:
    """Gets tokens list, calls ranker for each of them"""
    
    # final sorted by score docs
    final_docs = []

    # This dictionary contains doc_ids and their TF-IDF score
    doc_scores = {}

    for token in tokens:
        # The dictionary that contains term frequnecy of the word
        token_info = bool_search(token)
        # Number of all documents that contain token
        length = len(token_info)

        # A dictionary to purify original token_info
        final_dictionary = {}
        # If dictionary is too large, we only rank its
        # 10 members that have biggest values 
        if length > 10:
            for key in nlargest(10, token_info, key=token_info.get):
                final_dictionary[key] = token_info[key]

            ranker(doc_scores=doc_scores, length=length, token_info=final_dictionary)
        else:
            ranker(doc_scores=doc_scores, length=length, token_info=token_info)
        
    for pair in sorted(doc_scores.items(), key=lambda item: item[1]):
        final_docs.append(pair[0])
    
    # Reverse returns None!
    # Therefore we SHOULD NOT assign it to a var
    # We reverse the list to have descending order
    # This function modifies list directly
    final_docs.reverse()
    return final_docs
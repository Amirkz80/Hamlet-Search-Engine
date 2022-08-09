import math
import os
from datetime import datetime
from index import tokenizer
from boolean.boolean_operators import bool_search
from multiprocessing import Pool
from itertools import islice

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


def tf_idf_calculator(raw_term_frequency: int, docs_with_token_length: int) -> float:
    """Calculates the TF-IDF score of the given document and returns it"""

    return math.log10(1 + raw_term_frequency) * math.log10(len(os.listdir('repo/'))/(docs_with_token_length + 1))    


def ranker(doc_scores: dict, token_info: dict, length: int, start: int, end: int) -> list:
    """ranks the docs that contain token and returns list of
    relative docs that are sorted by TF-IDF """

    # doc_scores dictionary contains doc_ids and their TF-IDF score

    # Iterate over all docs that contain the token
    # They are in token term_frequncy dict (are the keys basically)
    #i = 1
    for doc_id in dict(islice(token_info.items(), start - 1, end)):
        t1 = datetime.now()
        
        if doc_id not in doc_scores:
            doc_scores[doc_id] = tf_idf_calculator(token_info[doc_id], length)
            #i += 1
            #print(datetime.now() - t1)
        else:
            doc_scores[doc_id] += tf_idf_calculator(token_info[doc_id], length)
        #print(datetime.now() - t1)
        #i += 1
    #print(i)

    return doc_scores

def rank_tokens(tokens: list) -> list:
    """Gets tokens list, calls ranker for each of them
    (call for each of them is done by Multiprocessing and 4 processes)
    Returns the sorted list for all tokens"""
    
    # final sorted by score docs
    final_docs = []

    # This dictionary contains doc_ids and their TF-IDF score
    doc_scores = {}

    for token in tokens:

        # The dictionary that contains term frequnecy of the word
        token_info = bool_search(token)
        # Number of all documents that contain token
        length = len(token_info.keys())

        groups = chunk(length, 4)
        ranges = [
            [doc_scores, token_info, length, groups[0][0], groups[0][1]],
            [doc_scores, token_info, length, groups[1][0], groups[1][1]],
            [doc_scores, token_info, length, groups[2][0], groups[2][1]],
            [doc_scores, token_info, length, groups[3][0], groups[3][1]],
        ]

        with Pool(4) as p:
            results = p.starmap(ranker, ranges)
            #print(f"results : {results}")
            for d in results:
                for key, value in d.items():
                    if key not in doc_scores:
                        doc_scores[key] = value
                    if key in doc_scores and value > doc_scores[key]:
                        doc_scores[key] = value 

    for pair in sorted(doc_scores.items(), key=lambda item: item[1]):
        final_docs.append(pair[0])
    
    # reverse returns None!
    # therefore we SHOULD NOT assign it to a var
    final_docs.reverse()
    # We reverse the list to have descending order
    # This function modifies list directly
    return final_docs
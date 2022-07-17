import os
import csv
import ast


def and_operator(first_docs_list: list, second_docs_list: list):
    """Returns results by executing AND operator on two input LISTS"""
    
    # This list saves the final result inside itself
    final_docs = []

    # If we didn't find any match for one keyword, there is no match at all
    # Return EMPTY LIST if there wasn't a match
    if (first_docs_list and second_docs_list) is False:
        return final_docs
    else:
        # Final list contains doc_IDs that are
        # In first_docs_list and second_docs_list  
        for doc in first_docs_list:
            if doc in second_docs_list:
                final_docs.append(doc)

    return final_docs


def or_operator(first_docs_list: list, second_docs_list: list):
    """Returns results by executing OR operator on two input LISTS"""

    # This list saves the final result inside itself
    final_docs = []

    # If we didn't find any match for both keywords, there is no match at all
    # Return EMPTY LIST if there wasn't a match
    if (first_docs_list or second_docs_list) is False:
        return final_docs
    else:
        # Final list contains doc_IDs that are
        # In first_docs_list or second_docs_list
        # We also check them to make sure they are not empty!
        if first_docs_list:
            for doc in first_docs_list:
                final_docs.append(doc)
        if second_docs_list:
            for doc in second_docs_list:
                # Prevents adding repeated docs to final_docs
                if doc not in final_docs:
                    final_docs.append(doc)
    
    return final_docs


def not_operator(docs_list: list):
    """Returns results by Executing NOT operator on the input LIST"""

    # This list saves the final result inside itself
    final_docs = [] 
    
    # There is no match for keyword, so its component is ALL DOC IDs
    if docs_list is False:
        return list(range(1, len(os.listdir('repo/')) + 1))
    else:
        for doc in list(range(1, len(os.listdir('repo/')) + 1)):
            if doc not in docs_list:
                final_docs.append(doc)
    
    return final_docs


def bool_search(keyword: str) -> dict:
    """Searches for the keyword in index_table,
    Returns term frequency dictioanry of the word"""

    dic = {}

    with open('index_table/index_table.txt', "r") as f:

        csv_reader = csv.DictReader(f)
        for line in csv_reader:
            if line['token'] == keyword.lower():
                
                # Change the string formatted dictionary, to python dict type
                dic =  ast.literal_eval(line['document_id_dic'])
                
    return dic
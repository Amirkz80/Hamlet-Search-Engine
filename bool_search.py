"""
In this script we perform booloean search
"""

import os
import csv
import ast
from datetime import datetime

def and_operator(first_keyword, second_keyword):
    """Returns results by Executing AND operator on two keywords"""
    
    # This list saves the final result inside itself
    final_docs = []

    # Searches for both keywords in index_table.txt 
    first_result =  bool_search(first_keyword)
    second_result =  bool_search(second_keyword)
    # If we didn't find any match for one keyword, there is no match at all
    # Return False if there wasn't a match
    if (first_result and second_result) is False:
        return False
    else:
        # Final list contains doc_IDs that are
        # In first_result['documents'] and second_result['documents']  
        for doc in first_result['documents']:
            if doc in second_result['documents']:
                final_docs.append(doc)

    return final_docs


def or_operator(first_keyword, second_keyword):
    """Returns results by Executing OR operator on two keywords"""

    # This list saves the final result inside itself
    final_docs = []

    # Searches for both keywords in index_table.txt 
    first_result =  bool_search(first_keyword)
    second_result =  bool_search(second_keyword)
    # If we didn't find any match for both keywords, there is no match at all
    # Return False if there wasn't a match
    if (first_result or second_result) is False:
        return False
    else:
        # Final list contains doc_IDs that are
        # In first_result['documents'] or second_result['documents']
        # We also check them to make sure they are not empty!
        if first_result:
            for doc in first_result['documents']:
                final_docs.append(doc)
        if second_result:
            for doc in second_result['documents']:
                # Prevents adding repeated docs to final_docs
                if doc not in final_docs:
                    final_docs.append(doc)
    
    return final_docs


def not_operator(keyword):
    """Returns results by Executing NOT operator on the keyword"""

    # This list saves the final result inside itself
    final_docs = []
    result = bool_search(keyword) 
    
    # There is no match for keyword, so its component is ALL DOC IDs
    if result is False:
        return list(range(1, len(os.listdir('repo/')) + 1))
    else:
        for doc in list(range(1, len(os.listdir('repo/')) + 1)):
            if doc not in result['documents']:
                final_docs.append(doc)
    
    return final_docs 


def bool_search(keyword):
    """Searches document with the specified keyword
    Returns IDs of documents if there was a match,
    and False if there wasn't any match"""

    with open('index_table/index_table.txt', "r") as f:

        csv_reader = csv.DictReader(f)
        for line in csv_reader:
            if line['token'] == keyword.lower():
                
                # We need to change the string formatted list, to a list type
                docs =  ast.literal_eval(line['document_id_list'])
                context = {'keyword': keyword, 'documents': docs}
                return context

    return False


def main():

    # Gets user input until user enters exit
    while 1:

        query = input("Enter a word, Enter 'exit' to exit : ")
        # To monitor duration time
        t1 = datetime.now()
        # Exit the program
        if query.lower() == 'exit':
            return 1
        # Search for keyword in file
        else:
            if ' AND ' in query:
                first_keyword = query[0:query.find(' AND ')]
                second_keyword = query[query.find(' AND ')+5:]
                result = and_operator(first_keyword, second_keyword)

                if result:
                    print(f"keyword: {query}, ID of DOCUEMNTS: {result}\n")
                else:
                    print("There wasn't a match!\n")
            
            elif ' OR ' in query:
                first_keyword = query[0:query.find(' OR ')]
                second_keyword = query[query.find(' OR ')+4:]
                result = or_operator(first_keyword, second_keyword)

                if result:
                    print(f"keyword: {query}, ID of DOCUEMNTS: {result}\n")
                else:
                    print("There wasn't a match!\n")

            elif 'NOT ' in query:
                keyword = query[query.find('NOT ')+4:]
                result = not_operator(keyword)

                print(f"keyword: {query}, ID of DOCUEMNTS: {result}\n")

            else:
                result = bool_search(query)
                if result:
                    print(f"keyword: {result['keyword']}, ID of DOCUEMNTS: {result['documents']}\n")
                else:
                    print("There wasn't a match!\n")
        
        print(
            f"searching index table time : ",
            f"{(datetime.now() - t1).total_seconds()}"
        )


if __name__ == "__main__":
    main()
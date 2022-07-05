"""This script makes an inverted
index list from the docs, so we can perform
boolean queries based on this list,
files in the repo directory are in .txt format
the output index_table.txt file is in csv format.

*** Note : This script needs to be executed first and
    before performing any search operation, we need its
    output (index_table.txt file) to do any search operation
***
"""

import os
import csv
from datetime import datetime

# Temporarily we save output indexes list in this dictionoary
# Before saving them in index_table.txt file 
indexed_list = {}
# Temporarily we save output documents list in this dictionoary
# Before saving them in doc_details.txt file
doc_IDs = {}


def tokenizer(word: str):
    """Cleans the input word, includes deleting everything except
    alphanumeric chars, converting word to lower format"""
    
    word = word.translate({
        ord(character): None for character in "!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\n\t\v\\"
        }
    ).lower()

    return word


def index_file(file_name, file_number):
    """Indexes file words by adding new words to the
    indexed_list, and also if a word is in another doc too,
    adds that documents's ID to word's document_ids_list"""
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            for word in line.split(' '):
                # Cleans up word
                word = tokenizer(word)
                # Add word if it wasn't already in the indexed_table
                if word not in indexed_list.keys():
                    indexed_list[word] = [file_number]
                # If there is a new doc containg word, add its ID to 
                # word's document_ids_list
                elif word in indexed_list.keys() and file_number not in indexed_list[word]:
                    indexed_list[word].append(file_number)


def files_surfer(directory=''):
    """Surfs in the given directory (which should be repo directory)
    Fills doc_IDs dicitonary by giving file
    name as key and file id as value"""
    
    # Increases as we index more documents 
    doc_id = 1

    # A list containg all files in the repo
    files_list = os.listdir(directory)
        
    for file in files_list:
        if file.endswith('.txt'):
            doc_IDs[file] = doc_id
            index_file(directory + file, doc_id)
            doc_id += 1


def main():
    """Controls main workflow of the program"""

    # To monitor duration time
    t1 = datetime.now()
    
    # Increases as we add more rows to csv rows
    word_num = 1

    # Start Surfing files in the documents directory,
    # Default is current index.the directory
    files_surfer(directory="repo/")

    # Delete Empty word row in indexes list, if it exists
    if '' in indexed_list.keys():
        del indexed_list['']

    # Make a file which contains detail about documents
    with open('index_table/doc_details.txt', 'w') as f:
        f.write("List of documents and their IDs:\n\n")
        for k, v in doc_IDs.items():
            f.write(f"doc: {k}, ID: {v}\n")

    # Save Dictionary in a file called index_table.txt with csv format
    with open('index_table/index_table.txt', 'w', newline="") as f:
        field_names = ['token_number', 'token', 'document_id_list']

        csv_writer = csv.DictWriter(f, fieldnames=field_names)
        csv_writer.writeheader()

        # Adding rows to file
        for k, v in sorted(indexed_list.items()):
            csv_writer.writerow({
                "token_number": word_num, "token": k, "document_id_list": v
                })
            word_num += 1
    
    # Total time that program took to finish the process 
    print(
        f"indexing all documents time : ",
        f"{(datetime.now() - t1).total_seconds()}"
    )

if __name__ == '__main__':
    main()
"""
In this script we perform booloean search
"""

from datetime import datetime
from ranking_functions import tokenize_query, ranker

def main():

    # Gets user input until user enters exit
    while 1:

        query = input("\nEnter the query, Enter 'exit' to exit : ")
        # To monitor duration time
        
        t1 = datetime.now()
        
        # Exit the program
        if query.lower() == 'exit':
            return 1
        
        else:
            # Cleans up the query, so we'll have raw strin
            # query = tokenizer(query)
            
            # Repeat the program if string is empty or None
            if (query.isspace() and query) or not query:
                print('\nquery can not be empty!')
            
            # Search for keyword in file
            else:
                
                # Tokenizing the query
                words = tokenize_query(query)
                print(ranker(words))

        print(
            f"searching index table time : ",
            f"{(datetime.now() - t1).total_seconds()}"
        )


if __name__ == "__main__":
    main()
"""
In this script we perform booloean search
"""
from datetime import datetime
from boolean_tokenizer import boolean_tokenize
from boolean_parser import shunting_yard, parse_query
from index import tokenizer

def main():

    # Gets user input until user enters exit
    while 1:

        query = input("Enter a word, Enter 'exit' to exit : ")
        # To monitor duration time
        
        t1 = datetime.now()
        
        # Exit the program
        if query.lower() == 'exit':
            return 1
        
        else:
            query = tokenizer(query)
            
            # Repeat the program if string is empty or None
            if (query.isspace() and query) or not query:
                print('query can not be empty!')
            
            # Search for keyword in file
            else:
                tokens = boolean_tokenize(query)
                postfix = shunting_yard(tokens)
                parsed_query = parse_query(postfix)
                print(sorted(parsed_query))


        print(
            f"searching index table time : ",
            f"{(datetime.now() - t1).total_seconds()}"
        )


if __name__ == "__main__":
    main()
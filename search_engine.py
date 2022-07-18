from datetime import datetime
import csv

# Flask related functions and classes
from flask import (
    jsonify,
    Flask, 
    redirect,
    render_template,
    request,
    url_for,
    send_from_directory,
    )

# Ranking search related functions
from ranking.ranking_functions import tokenize_query, ranker

# Boolean serch rekated fucntions
from boolean.boolean_tokenizer import boolean_tokenize
from boolean.boolean_parser import shunting_yard, parse_query
#from index import tokenizer

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    """Sends query to results function, with post method"""
    
    return redirect(url_for('results', query=request.get_json(force=True)['query']))


@app.route('/results/<string:query>', methods=['GET'])
def results(query):
    
    # To see the infromation retrieval duration
    t1 = datetime.now()
    # Saves returned docoment IDs
    doc_ids = []
    # Final document names
    results = []
    # Performs boolean retrieval if uppercase
    # operators were found in the query
    if ('AND' in query or
        'OR' in query or
        'NOT' in query):

        postfix = shunting_yard(boolean_tokenize(query))
        parsed_query = parse_query(postfix)
        doc_ids = sorted(parsed_query)
    
    # Performs ranked retireval
    else:
         doc_ids = ranker(tokenize_query(query))

    if doc_ids:
        print(doc_ids)
        with open('index_table/doc_details.txt', 'r') as f:
            csv_reader = csv.DictReader(f)
            lines = [line for line in csv_reader]
            for doc_id in doc_ids:
                for e in lines: 
                    if int(e['document_id']) == doc_id:
                        results.append(e['document_name'])
                        break
                    

    context = {
        # Returns total seconds in str format to (to make it serializable)
        'time': str((datetime.now() - t1).total_seconds()),
        'query': query,
        'results_length':len(results),
        'results': results
        }

    return jsonify(context)


@app.route('/files/<path:path>', methods=['GET'])
def get_file(path):
    return send_from_directory('repo', path)
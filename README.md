![hamlet_rectangle](https://user-images.githubusercontent.com/93945976/183778134-18b60488-dd77-4710-bebd-9911bb8ab46b.png)


# HAMLET
Hamlet is a search engine 🔎

<br>To be more specific it is a **Micro Search Engine** which is able to do 3 activities that are crucial for every search engine:
- **Crawling**
- **Indexing**
- **Ranking**

<br>It is able to crawl **English Wikipedia** and store the articles in text format, then it analyses all articles in the repository,
and in the final step it returns relevant results, based on the query that you give to hamlet.
<br>you can click on these results and you will be redirected to that result's page in WIKIPEDIA.

## How to search ?
Hamlet can detect whether to execute "**Boolean Search**" or "**Ranked Retrieval**".
<br><br>To perform a boolean search, all you need to do is to put an **UPPERCASE** boolean keyword inside your query. Hamlet realizes that there is an UPPERCASE boolean keyword and executes the boolean search.
<br>Supported boolean keywords are ---> "**AND**", "**OR**", "**NOT**", "**(**", "**)**"

<br>You can enter simple <e.g., "word1 AND word2"> or complex <e.g., "(word1 AND word2) OR ((NOT word3) AND word4 OR word5) OR (NOT word6))"> boolean queries, there is no limitation to use them,
<br>The only limitation is your imagination 🔮.

## ⭕💡NOTICE
<br>Remember, if you forget to use an UPPERCASE boolean keyword and use these keywords in lowercase mode, search engine doesn't execute the BOOLEAN SEARCH and only executes the RANKED RETRIEVAL.

## Example of ranked retrieval (with a test repository that contains 1011 random documents):
<br><img width="710" alt="Hamlet_Sample_1" src="https://user-images.githubusercontent.com/93945976/184540587-50847443-5d6c-44f1-8e9f-0492a7634c67.PNG">

## Example of boolean search (with a test repository that contains 1011 random documents):
<br><img width="691" alt="Hamlet_Sample_2" src="https://user-images.githubusercontent.com/93945976/184540540-5a6f5e53-dac1-4b85-ac09-914f3e664c3f.PNG">

# Set Up
Clone the project and by using command line navigate into the server folder, then create a virtual environment 
```
python -m venv <venv-name>
```
Activate this virtual environment by using the following commands
```
# On Linux
source <venv-name>/bin/activate
# On Windows
<venv-name>\scripts\activate
```
Now install dependencies in the requirements.txt
```
pip install -r requirements.txt
```
# Run Hamlet
## First Step: Crawler
Hamlet crawler, crawls 100 pages in each run time (**you can modify this amount by modifying wiki_crawler.py script**).
You can crawl Wikipedia by uisng two different approaches:
- Run "wiki_crawler.py" script in server folder, crawler will gather 100 articles from Wikipedia by default.
```
# While virtual environment is activated
python wiki_crawler.py
```
- Run "run_crawler.sh" script in server folder, this bash script will run "wiki_crawler.py" 100 times,<br>so the crawler will be able to gather 100 * 100 articles which is equal to 10000 articles. (**You can modify the amount of run times by changing the loop number in "run_crawler.sh"**)
```
bash run_crawler.sh
```
<br>All the gathered artices will be automatically placed in the "**repo**" folder.

## Second Step: Index Documents
Hamlet uses an inverted index list to perform different search methods on documents in the repository. "**index.py**" will do this action for us. Run "**index.py**" script in the server folder.
```
python index.py
```
It may take a while to index all documents, specially if you have a really large repository, but remember it is a fair cost to pay for having fast and related results in the next part, which is performing search action.

## Third Step: Setting Up The Front-End And The Back-End Server
First, by using command line navigate into the server folder then while the virtual environment is activated run the following commands, It will run a local development server:
```
set FLASK_APP=search_engine.py
set FLASK_ENV=development
flask run
```
Now by opening a new command line or terminal window, navigate into the client folder and run the following commands, this will activate our client side:
```
npm i
npm run dev
```

## Fourth Step: Enjoy searching 🎉🔎🌍
By using your browser go to <http://localhost:3000/>. 3000 is the next js default port which you can change if you want to.
you will observe a search box and that's it, have a nice search with hamlet 👨🏻‍💻👩🏻‍💻

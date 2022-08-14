![hamlet_rectangle](https://user-images.githubusercontent.com/93945976/183778134-18b60488-dd77-4710-bebd-9911bb8ab46b.png)


# HAMLET
Hamlet is a search engine 🔎

<br>To be more specific it is a **Micro Search Engine** which is able to do 3 activities that are crucial for every search engine:
- **Crawling**
- **Indexing**
- **Ranking**

<br>It is able to crawl **English Wikipedia** and store the articles in text format, then it analyses all articles in the repository,
and in the final step it returns relevant results, based on the query that you give to hamlet.

# Set Up
First by using command line navigate into the server folder, then create a virtual environment 
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
Second, by using command line navigate into the client folder and run the following commands, It will activate our client side:
```
npm i
npm run dev
```

## Fourth Step: Enjoy searching 🎉🔎🌍
Now by using the search box you can search by two dfferent approaches, **Boolean Search** or **Ranked Retrieval**

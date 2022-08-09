import requests
from bs4 import BeautifulSoup

n = 1
r = ''
called_num = 0

blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
]

def check_url(url):
    with open('index_table/urls.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    if url+'\n' in lines:
        return False
    else:
        return True

def parser(response):
    """A function to parse an html file"""
    return BeautifulSoup(response.text, 'html.parser')

def crawler(url: str):
    """A function to crawl a link's page"""
    
    global n
    global r
    global called_num
    
    called_num += 1

    # Making request to the url
    r = requests.get(url)

    with open(f'repo\{n}th file.txt', 'w', encoding="utf-8") as file:
            file.write(url + "\n")
            file.writelines([text + '\n' for text in parser(r).find_all(text=True) if text.parent.name not in blacklist and text != '\n'])
    
    n += 1
    with open('index_table/urls.txt', 'a', encoding='utf-8') as file:
        file.write(url + '\n')
        file.write(str(n) + '\n')

    print(url)

    for link in parser(r).find_all('a'):
        
        if called_num > 100:
            return 0
        elif link.get("href") is not None and "/wiki/" == link.get("href")[:6] and check_url("https://en.wikipedia.org" + link.get("href")) :
            crawler("https://en.wikipedia.org" + link.get("href"))

def main():
    """Main function"""
    global n
    with open('index_table/urls.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        n = int(lines[-1])
    print(f"n is equal to : {n}")
    crawler("https://en.wikipedia.org/wiki/Main_Page")

if __name__ == '__main__':
    main()
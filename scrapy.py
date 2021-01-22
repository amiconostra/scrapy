import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) < 2:
    print("USAGE: scrapy [Keyword]")
    exit(1)

def startScrapy():
    search = sys.argv[1]
    params = {'q': search}
    r = requests.get('https://www.bing.com/search', params=params)

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find('ol', {'id': 'b_results'})
    links = results.findAll('li', {'class': 'b_algo'})

    for link in links:
        link_text = link.find('a').text
        link_href = link.find('a').attrs['href']
        link_description = link.find('div', {'class': 'b_caption'}).find('p').text

        if link_text and link_href:
            print(link_text)
            print(link_href)
            print(link_description)
            print("----------------------------------------------")

startScrapy()
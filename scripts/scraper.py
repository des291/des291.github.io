import itertools
from bs4 import BeautifulSoup
import requests
import json
import itertools

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}


class ReadRss:

    def __init__(self, rss_url, headers, name):

        self.name = name
        self.url = rss_url
        self.headers = headers
        try:
            self.r = requests.get(rss_url, headers=self.headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', rss_url)
            print(e)
        try:
            self.soup = BeautifulSoup(self.r.text, 'lxml')
        except Exception as e:
            print('Could not parse the xml: ', self.url)
            print(e)
        self.articles = self.soup.findAll('item')[:10]
        self.articles_dicts = [{'title': a.find('title').text, 'link': a.link.next_sibling.replace('\n', '').replace(
            '\t', ''), 'description': a.find('description').text, 'pubdate': a.find('pubdate').text} for a in self.articles]
        self.urls = [d['link'] for d in self.articles_dicts if 'link' in d]
        self.titles = [d['title'] for d in self.articles_dicts if 'title' in d]
        self.descriptions = [d['description']
                             for d in self.articles_dicts if 'description' in d]
        self.pub_dates = [d['pubdate']
                          for d in self.articles_dicts if 'pubdate' in d]

    def to_json(self):
        output = self.articles_dicts
        # output = dict(itertools.islice(self.articles_dicts.items(), 7))
        with open(f'{self.name}.json', 'w') as file:
            json.dump(output, file)


bbc = ReadRss('https://feeds.bbci.co.uk/news/rss.xml?edition=uk',
              headers, 'bbc')
# print(bbc.articles_dicts)
# with open('bbc.json', 'w') as file:
#     json.dump(bbc.articles_dicts, file)
bbc.to_json()

guardian = ReadRss('https://www.theguardian.com/uk/rss', headers, 'guardian')
# print(guardian.articles_dicts)
guardian.to_json()

independent = ReadRss(
    'https://www.independent.co.uk/news/rss', headers, 'independent')
# print(independent.articles_dicts)
independent.to_json()

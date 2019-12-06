import requests
from bs4 import BeautifulSoup as bs
import json

list_of_urls = []
urls = ['https://us.boohoo.com/womens/coats-jackets?sz=20']

def jsonFile():
    data = []
    litsOfDict = []
    for url in urls:
        if url not in list_of_urls:
            response = requests.get(url)
            soup = bs(response.content, 'lxml')
            contents = soup.find_all('li', {'class': 'grid-tile'})
            dict = {}
            for content in contents:
                name = content.find('div', {'class': 'product-name'}).text
                price = content.find('span', {'class': 'product-sales-price'}).text[1:]
                image = content.find('img', {'content': True})['content']
                dict = {
                    'name': name,
                    'image': image,
                    'price': price,
                }
                litsOfDict.append(dict)
    # print(litsOfDict)
    data = json.dumps(litsOfDict)
    return data
# jsonFile()

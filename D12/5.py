import requests
import random
from bs4 import BeautifulSoup

def get_quote(key, language = 'ru', format = 'html'):

    url = f'http://api.forismatic.com/api/1.0/'

    payload  = {'method': 'getQuote', 'format': 'json', 'lang': 'ru', 'key': key}

    response = requests.get(url, params = payload)

    # http://api.forismatic.com/api/1.0/method=getQuote&key=457653&format=text&lang=ru

    # print(response.status_code)
    # print(response.text)

    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    print(response.json()['quoteText'])
    print(response.url)

if __name__ == '__main__':
    rand = random.randint(100000, 999999)
    get_quote(rand)

    # print(rand)




    


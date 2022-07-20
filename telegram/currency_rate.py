import requests
from bs4 import BeautifulSoup

URL = 'https://www.nbkr.kg/index.jsp?lang=RUS'

def get_html(url):
    response = requests.get(url).text
    return response

def get_data(table):
    names = table.find_all('td', class_='excurr')
    prices = table.find_all('td', class_='exrate')
    names_ = [i.text for i in names if '/' in i.text]
    prices_ = [i.text for i in prices]
    converter = {
        names_[0]: prices_[0],
        names_[1]: prices_[2],
        names_[2]: prices_[4],
        names_[3]: prices_[6],
    }
    return converter


def get_table(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('div', class_='sticker-body')
    return table[2]


def write_to_json(data):
    import json
    with open('/home/abai/Desktop/shop_shoes/Hackaton_back/telegram/rate.json', 'w') as file:
        json.dump(data, file, indent=4)

def parse():
    html = get_html(URL)
    table = get_table(html)
    data = get_data(table)
    write_to_json(data)

if __name__ == '__main__':
    parse()
    


import requests
from bs4 import BeautifulSoup
import fake_useragent
import json
import datetime

from pprint import pprint


def get_branch():
    ua =fake_useragent.UserAgent()

    headers = {
        'accept': 'application/json, text/plain, */*',
        'user-Agent': ua.google,
    }

    for i in range(1):
        url = f'https://www.rsk.kg/ru/points'

        req = requests.get(url, headers=headers).text

        soup = BeautifulSoup(req, 'lxml')
        pprint(soup)
        # all_branch_name = soup.find_all('div', attrs={"class": "tab-content"}) # получаем филиалы
        try:
            name = soup.find('ol', attrs={"class": "point-list list-unstyled"}).text #Название филиала
        except:
            name = "пусто"
        try:
            region = soup.find('ol', attrs={"class": "point-list list-unstyled"}).text #Область
        except:
            region = "пусто"
        try:
            address = soup.find('ol', attrs={"class": "point-list list-unstyled"}).text #адрес
        except:
            address = "пусто"
        try:
            phone = soup.find('ol', attrs={"class": "point-list list-unstyled"}).text #телефон
        except:
            phone = "пусто"
        branch = {
            "name":name,
            "region":region,
            "address":address,
            "phone":phone
        }
        pprint(name)
        return branch

if __name__ == "__main__":
   with open(f"json/branch_{datetime.datetime.now().strftime('%d_%m_%Y')}.json", "w", encoding='utf-8') as f:
        try:
            json.dump(get_branch(), f, indent=4, ensure_ascii=False)
            print('Филиалы добавлены')
            print(get_branch)
        except:
            print('Филиалы не удалось получить')

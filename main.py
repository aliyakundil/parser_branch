import requests
from bs4 import BeautifulSoup
import fake_useragent
import json
import datetime, time

from pprint import pprint

from selenium import webdriver

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



def get_source_html(url):
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(
    #     executable_path = 'chromedriver/chromedriver.exe'
    # )
    # driver.get('https://www.rsk.kg/ru/points');

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

    while True:
        find_more_element = driver.find_element("tab region_9 active")
        actions = ActionChains(driver)
        actions.move_to_element(find_more_element).perform()
        time.sleep(3)
def main():
    get_source_html(url='https://www.rsk.kg/ru/points')

if __name__ == '__main__':
    main()

# def get_branch():
#     ua =fake_useragent.UserAgent()
#
#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'user-Agent': ua.google,
#     }
#
#     for i in range(1):
#         url = f'https://www.rsk.kg/ru/points'
#
#         req = requests.get(url, headers=headers).text
#
#         soup = BeautifulSoup(req, 'lxml')
#         pprint(soup.div)
#         # all_branch_name = soup.find_all('div', attrs={"class": "tab-content"}) # получаем филиалы
#         try:
#             name = soup.find_all('div', attrs={"class": "tab region_9 active"}) #Название филиала
#         except:
#             name = "пусто"
#         try:
#             region = soup.find('ol', attrs={"class": "point-list list-unstyled"}).text #Область
#         except:
#             region = "пусто"
#         try:
#             address = soup.find('ol', attrs={"class": "point-list list-unstyled"}).text #адрес
#         except:
#             address = "пусто"
#         try:
#             phone = soup.find('ol', attrs={"class": "point-list list-unstyled"}).text #телефон
#         except:
#             phone = "пусто"
#         branch = {
#             "name":name,
#             "region":region,
#             "address":address,
#             "phone":phone
#         }
#         pprint(name)
#         return branch
#
# if __name__ == "__main__":
#    with open(f"json/branch_{datetime.datetime.now().strftime('%d_%m_%Y')}.json", "w", encoding='utf-8') as f:
#         try:
#             json.dump(get_branch(), f, indent=4, ensure_ascii=False)
#             print('Филиалы добавлены')
#             print(get_branch)
#         except:
#             print('Филиалы не удалось получить')

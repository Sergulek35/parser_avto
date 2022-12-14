import json
import requests
from bs4 import BeautifulSoup
import pprint

result = {}
links = {}
car_brands = {'марки': [],
              'модификация': []}

url = 'http://avantaauto.ru'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for cars_tag in soup.find_all('div', class_='col-lg-3 col-md-4 col-sm-6'):
    title_tag = cars_tag.find('div', class_='hit-card__title')
    title = title_tag.text.replace('\n', '').strip()

    price_tag = cars_tag.find('p', class_='hit-card__price')
    price = price_tag.text.replace('\n', '').replace('     ', ' ').strip()

    result[title] = price
    imgs_tag = cars_tag.find('div', class_='hit-card__img')
    imgs = imgs_tag.prettify().replace('"', '').replace('>', '').replace('title=', '').replace('data-img-hover=',
                                                                                               'http://avantaauto.ru').split()
    links[imgs[4]] = imgs[-4]

car_brands['марки'].append(result)
car_brands['модификация'].append(links)

print('     ХИТЫ ПРОДАЖ ОТ "AVANTA"', url)
print('- -' * 20)
pprint.pprint(car_brands)

with open('car_brands.json', 'w') as f:
    json.dump(car_brands, f)

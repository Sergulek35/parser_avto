import json
import requests
from bs4 import BeautifulSoup





def separator(simbol):
    return simbol * 20


def parce_car():

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
    car_brands['модификация'].append(f'{links}')

    titles = f'     ХИТЫ ПРОДАЖ ОТ "AVANTA" {url}'

    with open('car_brands.json', 'w') as f:
        json.dump(car_brands, f)

    with open('car_brands.txt', 'w') as f:
        f.write(f'{car_brands}')

    return  titles, separator('- -'), car_brands
import pprint
import requests


def get_id_region(url_area='https://api.hh.ru/areas/113', val='Уфа'):
    """
    возвращаем ID города
    :param DOMAIN:
    :param val:
    :return:
    """
    response = requests.get(url_area).json()
    for cities in response['areas']:
        for city in cities['areas']:
            if city['name'] == val:
                return city['id']  # , city['parent_id'], cities['name']

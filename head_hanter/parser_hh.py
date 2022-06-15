import requests
import time

import head_hanter.stat_orm2


def parser(stat, region_id=99, search_bar='python Developer'):
    url_vacancies = 'https://api.hh.ru/vacancies'
    num = 0
    start_page = 0
    while True:
        params = {
            'text': search_bar,
            'per_page': 50,
            'page': start_page,
            'area': region_id
        }
        response = requests.get(url_vacancies, params=params).json()

        items = response['items']
        if len(items) == 0:
            print('Поиск завершен')
            break

        for item in items:  # список словарей   -> текущий словарь
            result = requests.get(item['url']).json()
            head_hanter.stat_orm2.find(result['key_skills'])
            # num += stat.find(result['key_skills'])  # сбор статистики
        print(f'Поиск по стрнице {start_page}, обнаружено {num} совпадений')
        start_page += 1
        # time.sleep(1)  # Задержка
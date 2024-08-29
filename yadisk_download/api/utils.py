import requests

from urllib.parse import urlencode
from django.core.cache import cache

RESOURCES = "https://cloud-api.yandex.net/v1/disk/public/resources?"


def get_files_from_yadisk_link(link: str) -> list[dict]:
    '''
    принимает ссылку, парсит ее и возвращает список объектов
    с полями вида
    [{
        'filename': 'имя файла',
        'link': 'ссылка_на_скачивание_файла'
    },]
    Использует кэш, если ссылка проверялась - повторной проверки не будет
    '''
    requests_url = RESOURCES + urlencode(dict(public_key=link))
    cached_links = cache.get(link)

    if cached_links is not None:
        return cached_links

    response = requests.get(requests_url)
    type = response.json()['type']

    if type == 'dir':
        links_list = []
        files_list = response.json()['_embedded']['items']
        for file in files_list:
            links_list.append({
                'filename': file['name'],
                'link': file['file']
            })

    else:
        file = response.json()
        links_list = [{
            'filename': file['name'],
            'link': file['file']
        }]

    cache.set(link, links_list)
    print('not cashed')
    return links_list

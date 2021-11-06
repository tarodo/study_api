import os

from urllib.parse import urlparse

import requests

from dotenv import load_dotenv

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("user_link", help="link to check or make it bit")
args = parser.parse_args()

load_dotenv()

BIT_URL = 'https://api-ssl.bitly.com/v4'
bit_token = os.getenv('BIT_TOKEN')


def shorten_link(token: str, url: str) -> str:
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        "domain": "bit.ly",
        "long_url": url
    }
    response = requests.post(f'{BIT_URL}/shorten', headers=headers, json=payload)
    response.raise_for_status()
    bitlink_data: dict = response.json()

    return bitlink_data['link']


def base_bitlink_link(url: str) -> str:
    url_parts = urlparse(url)
    return f'{BIT_URL}/bitlinks/{url_parts.netloc}{url_parts.path}'


def count_clicks(token: str, url: str) -> int:
    headers = {'Authorization': f'Bearer {token}'}
    params = {'unit': 'day', 'units': '-1'}
    response = requests.get(f'{base_bitlink_link(url)}/clicks/summary',
                            headers=headers, params=params)
    response.raise_for_status()
    clicks_data: dict = response.json()

    return clicks_data['total_clicks']


def is_bitlink(token: str, url: str) -> bool:
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(base_bitlink_link(url), headers=headers)
    return response.ok


if __name__ == "__main__":
    user_url = args.user_link

    try:
        if is_bitlink(bit_token, user_url):
            clicks_count = count_clicks(bit_token, user_url)
            print(f'Всего кликов: {clicks_count}')
        else:
            bitlink = shorten_link(bit_token, user_url)
            print(f'Битлинк: {bitlink}')
    except requests.exceptions.HTTPError:
        print('Ошибка. Ваша ссылка не валидна')

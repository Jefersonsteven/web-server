import requests
from requests import RequestException

def get_categories():
    try:
        response = requests.get('https://api.escuelajs.co/api/v1/categories/')
        data = response.json()
        return data
    except RequestException as error:
        return error
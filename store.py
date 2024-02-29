from icecream import ic as print
import requests

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories/')
    data = response.json()
    print(data)
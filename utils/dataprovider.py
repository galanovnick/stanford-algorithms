import requests

chrome_headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def get(url: str) -> str:
    response = requests.get(url, headers=chrome_headers)
    return response.content.decode("utf-8")

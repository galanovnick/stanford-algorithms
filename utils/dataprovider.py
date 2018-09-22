from urllib import request


def get(url: str) -> str:
    response = request.urlopen(url).read()
    return response.decode("utf-8")

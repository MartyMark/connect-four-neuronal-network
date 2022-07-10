import requests


def get(url, query=None):
    response = requests.get(url, params=query)

    print(response.text)
    print(response.content)


def post(url, data):
    requests.post(url, data)


def put(url, data):
    requests.put(url, data)

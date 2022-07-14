import requests


def get(url, query=None):
    return requests.get(url, params=query)


def post(url, data):
    requests.post(url, data)


def put(url, data):
    requests.put(url, data)

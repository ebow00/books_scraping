import requests


class BookWebPage:

    def __init__(self, url):
        self.url = url

    @property
    def content(self):
        return requests.get(self.url).content

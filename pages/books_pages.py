from bs4 import BeautifulSoup

from locators.book_page_locators import BooksLocators

from parsers.book import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        locator = BooksLocators.PAGE_COUNT
        counter_string = self.soup.select_one(locator).string.strip()
        counter_string_trunc = counter_string[counter_string.find('of ') + 3:]
        return int(counter_string_trunc)

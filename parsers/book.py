from locators.books_locators import BooksLocators
from pages.individual_book_page import IndividualBookPage
from web_pages.books_web_page import BookWebPage


class BookParser:
    """
    Given one specific book article tag, find out the data about the book (book title, link, price and rating).
    Except for category
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        if self.rating == 1:
            return f'<Bk: {self.title}, lnk: {self.link}, prc: {self.price}, rtg: {self.rating} star, category>'
        else:
            return f'<Bk: {self.title}, lnk: {self.link}, prc: {self.price}, rtg: {self.rating} stars, category>'

    BOOK_PAGE_URL_PREF = "https://books.toscrape.com/catalogue/"

    @property
    def title(self):
        locator = BooksLocators.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def link(self):
        locator = BooksLocators.LINK
        return self.parent.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = BooksLocators.PRICE
        return self.parent.select_one(locator).string

    @property
    def rating(self):
        rating_map = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        locator = BooksLocators.RATING
        return rating_map[self.parent.select_one(locator).attrs['class'][1]]

    @property
    def category(self):
        """
        This method is not working well and still needs much more complex debugging. I'm still waiting for a reply from
        the course team about it
        :return:
        The book category in the form of a string
        """
        book_page_url = f'{self.BOOK_PAGE_URL_PREF}{self.link}'
        book_page = BookWebPage(book_page_url)
        content = book_page.content
        category = IndividualBookPage(content).category
        return category

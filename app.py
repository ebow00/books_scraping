from pages.books_pages import BooksPage
from web_pages.books_web_page import BookWebPage

page = BooksPage(BookWebPage("https://books.toscrape.com/catalogue/page-1.html").content)
books = page.books

for page_num in range(1, page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page = BooksPage(BookWebPage(url).content)
    books.extend(page.books)

for book in books:
    print(book)

# print(page.page_count)

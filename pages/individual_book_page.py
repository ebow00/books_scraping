from bs4 import BeautifulSoup

from locators.breadcrumbs_locator import BreadcrumbLocator


class IndividualBookPage:
    def __init__(self, ind_page):
        self.soup = BeautifulSoup(ind_page, 'html.parser')

    @property
    def category(self):
        locator_list = BreadcrumbLocator.BREADCRUMB_LIST
        locator_bc = BreadcrumbLocator.BREADCRUMB
        bc_list = self.soup.select(locator_list)[-2]
        cat_cat = bc_list.select_one(locator_bc).string
        if cat_cat:
            return cat_cat
        else:
            return "No string"

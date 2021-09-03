"""
This is the file for PageObject model. There are all actions execute on the
web-pages are here.
"""

from webdriver import *
from locators import Locators as L
from urllib.parse import urlparse
from webdriver import Driver


class BasePage():

    def startWork(self, browser, url):
        self.browser = Driver.__init__()
        self.browser.goToStartPage(self.browser, url)
        self.browser.loadCookies(self.browser, filename="cookies")

        # Use method below in the first run and do login to the site to save
        # your cookies (comment loadCookies method before).
        # self.browser.saveCookies(filename="cookies")


class HomePageObject(BasePage):

    # def __init__(self):
    #     super().__init__()

    def startSearch(self, keywords: str):
        self.browser.findElementByXpath(By.XPATH, L.search_box_xpath)
        self.browser.writeText(self.browser, keywords)
        self.browser.pushKeys(self.browser)


class SearchPageObject(BasePage):

    # def __init__(self):
    #     super().__init__()

    def checkCurrentUrl(self):
        self.current_url = self.browser.current_url(self.browser)
        self.current_url_path = urlparse(self.current_url).path

    def checkPage(self):
        if self.current_url_path.startswith("applicant"):
            self.browser.previous_page(self.browser)
            self.browser.findElementByXpath(By.XPATH, L.mark_favorites).click()
        elif self.current_url_path.startswith("search"):
            pass
            if self.browser.findElementByClassName(By.CLASS_NAME,
                                                   L.cover_letter_iframe_class):
                self.browser.previous_page(self.browser)
                self.browser.findElementByXpath(By.XPATH,
                                                L.mark_favorites).click()
        else:
            return print("Path check error.")

    def scrollDownAndApply(self):
        submit_apply_buttons = self.browser.findElementByXpath(By.XPATH,
                                                               L.apply_button_xpath).click()

    while submit_apply_buttons:
        for button in submit_apply_buttons:
            driver.execute_script("arguments[0].scrollIntoView();",
                                  submit_apply_buttons)
            driver.execute_script("(arguments[0]).click();",
                                  submit_apply_buttons)

    def checkMarkFavorites(self):
        mark = driver.find_element(By.XPATH, L.mark_favorites)
        if mark == "vacancy-search-mark-favorite_false":
            pass  # .click() для добавление в избранное
        else:
            pass

    def goToNextPage(self):
        # driver.find_element(By.XPATH, 'a[@data-qa="pager-page"]/span')
        pass

"""
This file contains all about webdriver.
"""

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Driver():

    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference('dom.webnotifications.enabled', False)
        self.options.set_preference('media.volume_scale', '0.0')
        instance = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def goToStartPage(self, instance, url):
        instance.get(url)
        instance.implicitly_wait(10)

    def saveCookies(self, instance, filename: str):
        pickle.dump(instance.get_cookies(), open(filename, 'wb'))

    def loadCookies(self, instance, filename: str):
        for cookie in pickle.load(open(filename, 'rb')):
            instance.add_cookie(cookie)
        instance.refresh()

    def findElementByXpath(self, instance, locator, path=By.XPATH):
        instance.find_element(path, locator)

    def findElementByClassName(self, instance, locator, path=By.CLASS_NAME):
        instance.find_element(path, locator)

    def writeText(self, instance, keywords):
        instance.send_keys(keywords)

    def pushKeys(self, instance, keys=Keys.ENTER):
        instance.send_keys(keys)

    def current_url(self, instance):
        instance.current_url()

    def cover_letter_iframe(self, instance, locator, path=By.CLASS_NAME,):
        instance.find_element(path, locator)

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

    def setDriverOptions(self):

        self.options = webdriver.FirefoxOptions()
        self.options.set_preference('dom.webnotifications.enabled', False)
        self.options.set_preference('media.volume_scale', '0.0')

    def initDriverInstance(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def goToStartPage(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def saveCookies(self, filename: str):
        pickle.dump(self.driver.get_cookies(), open(filename, 'wb'))

    def loadCookies(self, filename: str):
        for cookie in pickle.load(open(filename, 'rb')):
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def findElementByXpath(self, arg):
        self.driver.find_element(By.XPATH, arg)

    def findElementByClassName(self, arg):
        self.driver.find_element(By.CLASS_NAME, arg)

    def writeText(self, instance, keywords):
        instance.send_keys(keywords)

    def pushKeys(self, instance, keys=Keys.ENTER):
        instance.send_keys(keys)
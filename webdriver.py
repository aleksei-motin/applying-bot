"""
This file contains all about webdriver.
"""

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

options = webdriver.FirefoxOptions()
options.set_preference('dom.webnotifications.enabled', False)
options.set_preference('media.volume_scale', '0.0')
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

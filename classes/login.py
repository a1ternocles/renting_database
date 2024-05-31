import requests
import urllib.parse 
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Login():

    def __init__(self):
        
        self.website = None
        self.base_url = None
        self.partial_url = None
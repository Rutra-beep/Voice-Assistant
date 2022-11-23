from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.webdriver.common.by import By


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        print(enter)
        enter.click()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.webdriver.common.by import By


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def play(self, query):
        self.query = query
        self.driver.get(url=f'https://www.youtube.com/results?search_query={query}')
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        video.click()


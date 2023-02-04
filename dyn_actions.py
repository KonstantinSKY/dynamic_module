#!/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Actions:

    def __init__(self, drv):
        self.driver = drv

    def find(self):
        input_ = self.driver.find_element(By.TAG_NAME, 'input')
        input_.send_keys('ChromeDriver is the BEST NEW')
        sleep(5)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    actions = Actions(driver)
    actions.find()
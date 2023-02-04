#!/bin/python

#!/bin/python
import importlib
from selenium import webdriver
import multi_import as mu

print("""Test import module for dynamic import other module
            You can check CONST in check module, save module, and push anykey for to see new value))
        """)
#TODO CREATE timer!!!

if __name__ == '__main__':
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.google.com/')
    menu_module = mu.import_one("menu")
    while True:
        menu = menu_module.Menu(driver)
        menu.display()
        mu.reload(menu_module)
        print("Next loop of menu")
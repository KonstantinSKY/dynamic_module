#!/bin/python

#!/bin/python
import importlib
from selenium import webdriver
print("""Test import module for dynamic import other module
            You can check CONST in check module, save module, and push anykey for to see new value))
        """)


if __name__ == '__main__':
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.google.com/')
    menu_module = importlib.import_module("menu")
    while True:
        menu = menu_module.Menu()
        menu.display()
        importlib.reload(menu_module)

#!/bin/python

#!/bin/python
import importlib
import menu
print("""Test import module for dynamic import other module
            You can check CONST in check module, save module, and push anykey for to see new value))
        """)


if __name__ == '__main__':

    menu_module = importlib.import_module("menu")
    while True:
        menu = menu_module.Menu()
        menu.display()
        importlib.reload(menu_module)

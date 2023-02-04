#!/bin/python

from python_console_menu import AbstractMenu, MenuItem
from time import sleep

import multi_import as mu


def test_func():
    print("This is a test Function!!")
    sleep(5)

def test_func_2():
    print("This is a test Function_22222222!!")
    sleep(5)

actions_module = mu.import_one("dyn_actions")


class Menu(AbstractMenu):
    def __init__(self, drv):
        super().__init__("Welcome to the menu.")
        self.driver = drv
        self.actions = actions_module.Actions(self.driver)


    def initialise(self):
        self.add_menu_item(MenuItem(0, "Reload the menu", lambda: mu.reload(actions_module)).set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Start function", lambda: print("menu=DemoSubMenu!!!!")))
        self.add_menu_item(MenuItem(2, "Hidden menu item", lambda: print("I was a hidden menu item")))
        self.add_menu_item(MenuItem(3, "New menu item", lambda: print("I was a new menu item")))
        self.add_menu_item(MenuItem(4, "Test function", lambda: test_func()))
        self.add_menu_item(MenuItem(5, "Test function222", lambda: test_func_2()))
        self.add_menu_item(MenuItem(6, "ACtions Test", lambda: self.actions.find()))


if __name__ == '__main__':
    menu = Menu("drv tipo")
    menu.display()

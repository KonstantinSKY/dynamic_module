#!/bin/python

from python_console_menu import AbstractMenu, MenuItem


class Menu(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "Exit menu").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Start function", lambda: print("menu=DemoSubMenu!!!!")))
        self.add_menu_item(MenuItem(3, "Hidden menu item", lambda: print("I was a hidden menu item")))
        self.add_menu_item(MenuItem(4, "New menu item", lambda: print("I was a new menu item")))
        self.add_menu_item(MenuItem(5, "5 New menu item", lambda: print("55555 a new menu item")))


if __name__ == '__main__':
    menu = Menu()
    menu.display()

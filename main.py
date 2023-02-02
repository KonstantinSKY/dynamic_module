#!/bin/python
import importlib


if __name__ == '__main__':

    module = importlib.import_module("test_module")
    while True:
        print(module.CONST)
        anykey = input("You can update you module file and anykey for reload it")

        importlib.reload(module)


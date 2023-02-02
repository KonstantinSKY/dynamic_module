#!/bin/python
import importlib
print("""Test import module for dynamic import other module
            You can check CONST in check module, save module, and push anykey for to see new value))
        """)


if __name__ == '__main__':

    module = importlib.import_module("test_module")
    while True:
        print(module.CONST)
        anykey = input("You can update you module file and anykey for reload it")

        importlib.reload(module)


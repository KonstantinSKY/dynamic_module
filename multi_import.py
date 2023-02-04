#!/bin/python

import importlib
import traceback


# class Multi_import:
#      def __init__(self, **args):
#         for arg in args:


def import_one(module):
    print("Importing module:", module)
    return importlib.import_module(module)


def import_all(*modules):
    res = list()
    for module in modules:
        res.append(import_one(module))
    return res


def reload(module):
    try:
        print("Reloading module ...:", module)
        importlib.reload(module)
    except Exception as err:
        print(f"During reloading was error:\n {err=}\n, {type(err)=}")
        traceback.print_exc()
        print("YOU can fix this error and continue by anykey ...")
        print("Error module will be reload again but webdriver will work without interceptions...")
        anykey = input()
        reload(module)


def reload_all(*modules):
    for module in modules:
        reload(module)


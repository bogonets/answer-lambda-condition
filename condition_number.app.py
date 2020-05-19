# -*- coding: utf-8 -*-

import numpy as np
import time
import sys


symbol = "=="


def on_set(key, val):
    if key == "symbol":
        global symbol
        symbol = val


def on_get(key):
    if key == "symbol":
        return symbol


def on_init():
    return True


def on_valid():
    return True


def on_run(number1, number2):
    # sys.stdout.write(f"[ConditionNumber] nubmer1: {number1} \n")
    # sys.stdout.write(f"[ConditionNumber] nubmer2: {number2} \n")
    # sys.stdout.flush()
    result = eval(f"{number1[0]}{symbol}{number2[0]}")
    
    # sys.stdout.write(f"[ConditionNumber] result: {result} \n")
    # sys.stdout.flush()
    return {'condition': np.array([result], np.int32)}


def on_destroy():
    return True


if __name__ == '__main__':
    pass

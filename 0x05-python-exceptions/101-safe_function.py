#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as e:
        res = None
        print("Exception: {}".format(e), file=stderr)
    finally:
        return res

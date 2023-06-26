#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except BaseException as be:
        print("Exception: {}".format(be), file=sys.stderr)
        return False

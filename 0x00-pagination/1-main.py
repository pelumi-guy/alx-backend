#!/usr/bin/env python3
"""
Main file
"""
from pprint import pprint

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


pprint(server.get_page(1, 3))
pprint(server.get_page(3, 2))
pprint(server.get_page(3000, 100))
pprint(server.get_page(195, 100))
pprint(server.get_page(196, 100))

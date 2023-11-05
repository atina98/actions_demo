#!/usr/bin/env python3

"""
Simple "Hello World!" Testing Program
"""

import unittest
from hello_world import Greeting

class MyTest(unittest.TestCase):
    greeting = Greeting()
    self.assertEqual(greeting.message, "Hello World!")

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

"""
Simple "Hello World!" Testing Program
"""

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual("Hello World!")
import os
import unittest


def additional_tests():
    root_path = os.path.abspath(os.path.dirname(__file__))
    return unittest.defaultTestLoader.discover(root_path)
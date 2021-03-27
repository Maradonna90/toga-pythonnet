import unittest
from main import App
import time


class Test_Toga(unittest.TestCase):
    def test_vanilla(self):
        app = App()
        app.create()

    def test_patched(self):
        pass

import unittest
from main import App
import time


class Test_Toga(unittest.TestCase):
    def test_vanilla(self):
        app = App()
        app.create()
        time.sleep(5)
        app.exit()

    def test_patched(self):
        pass

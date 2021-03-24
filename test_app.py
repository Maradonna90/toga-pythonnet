import unittest
import main


class Test_Toga(unittest.TestCase):
    def test_vanilla(self):
        main.App()

    def test_patched(self):
        pass

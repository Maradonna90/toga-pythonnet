import unittest
import main


class Test_Toga(unittest.TestCase):
    def test_vanilla(self):
        main.main()

    def test_patched(self):
        pass

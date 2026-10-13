import unittest

def uzemanyag(a:int,b:float):
    return(round((b/a)*100,2))

class TestUzemAnyag(unittest.TestCase):
    def test_egy_pozitiv(self):
        self.assertEqual(uzemanyag(767,40.38),5.26)

    def test_egy_negativ(self):
        self.assertEqual(uzemanyag(-767,40.38),-5.26)

    def test_pozitiv(self):
        self.assertGreater(uzemanyag(767,40.38),0)

    def test_negativ(self):
        self.assertLess(uzemanyag(-767,40.38),0)

unittest.main()
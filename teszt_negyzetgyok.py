import math
import unittest


def negyzetgyok(sz:int):
    if sz > 0:
        return(math.sqrt(sz))
    else:
        return("Negativ szambol nem vonunk negyzetgyokot!")

class TestNegyzetgyok(unittest.TestCase):

    def test_egy_pozitiv(self):
        ertek = negyzetgyok(4)
        self.assertEqual(ertek,2)

    def test_negativ(self):
        ertek = negyzetgyok(-1)
        self.assertEqual(ertek,"Negativ szambol nem vonunk negyzetgyokot!")

    def test_pozitiv(self):
        ertek = negyzetgyok(7)
        self.assertGreater(ertek,0)

unittest.main()

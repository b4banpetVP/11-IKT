import unittest

def paros_szamok(also:int,felso:int):  
    osszeg = 0
    if also > 0 and felso > 0:
        for i in range(also,felso+1):
            if i%2 == 0:
                osszeg += i
    else:
        for i in range(felso,also+1):
            if i%2 == 0:
                osszeg += i

    return(osszeg)
class TestParosSzamok(unittest.TestCase):
    def test_pozitiv(self):
        self.assertGreater(paros_szamok(5,9),0)

    def test_egy_pozitiv(self):
        self.assertEqual(paros_szamok(5,9),14)
    
    def test_egy_negativ(self):
        self.assertEqual(paros_szamok(-5,-9),-14)
    


import unittest
def szamologep(elso:float,masodik:float,muvelet:str):
    if muvelet == "+":
        return(elso + masodik)
    elif muvelet == "-":
        return(elso - masodik)
    elif muvelet == "*":
        return(elso * masodik)
    elif muvelet == "/":
        if masodik == 0:
            return("Ejnye, nullaval nem osztunk!")
        else:
            return(elso / masodik)
    else:
        return("Hibas muveleti jel!")

class TesztSzamologep(unittest.TestCase):

    def test_pozitiv(self):
        self.assertGreater(szamologep(4,7,"+"),0)

    def test_egy_pozitiv(self):
        self.assertEqual(szamologep(4,7,"+"),11)

    def test_negativ(self):
        self.assertLess(szamologep(4,7,"-"),0)

    def test_egy_negativ(self):
        self.assertEqual(szamologep(4,7,"-"),-3)

    def test_nullaval_oszt(self):
        self.assertEqual(szamologep(5,0,"/"),"Ejnye, nullaval nem osztunk!")

unittest.main()
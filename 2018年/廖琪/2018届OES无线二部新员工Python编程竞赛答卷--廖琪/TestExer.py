import unittest
from exer import CmpStr

class TestExer(unittest.TestCase):
        
    def test_1(self):
        self.assertEquals(CmpStr("dsfjho ;]//'","1276shajy"),-2)
        self.assertEquals(CmpStr("djau92749sdfhkia"," kjshfia;  "),-2)
        self.assertEquals(CmpStr("JWUI8 ka  .,'","sjh867/.']"),-2)
        
    def test_2(self):
        self.assertEquals(CmpStr('dsfjho','dsfj'),1)
        self.assertEquals(CmpStr('ajkue','ajkueknui'),-1)
        self.assertEquals(CmpStr('jkbhfq','jkbhfq'),0)
        
    def test_3(self):
        self.assertEquals(CmpStr('3845719','384'),1)
        self.assertEquals(CmpStr('9858701','985870100'),-1)
        self.assertEquals(CmpStr('3451893','3451893'),0)
        
    def test_4(self):
        self.assertEquals(CmpStr('00028749','0287'),1)
        self.assertEquals(CmpStr('0038401','0040000'),-1)
        self.assertEquals(CmpStr('0034','034'),1)
        self.assertEquals(CmpStr('000923789','000000923789'),-1)
        self.assertEquals(CmpStr('0000273817','0000273817'),0)
        
    def test_5(self):
        self.assertEquals(CmpStr('qhjbak','73286'),1)
        self.assertEquals(CmpStr('78236741','akhfiu'),-1)
        
    def test_6(self):
        self.assertEquals(CmpStr('184769jkhiwhr','9187501750175'),1)
        self.assertEquals(CmpStr('73467hfihgi','hfihgiqeuiy'),-1)
        self.assertEquals(CmpStr('198791hguw','h'),1)
        self.assertEquals(CmpStr('897jhfi','jhfi'),0)
        self.assertEquals(CmpStr('hgjfh18','913'),1)
        self.assertEquals(CmpStr('kjhqi389174','kjhqijdki'),-1)
        self.assertEquals(CmpStr('jhvckh10948','jhv'),1)
        self.assertEquals(CmpStr('ajkbhi9814087','ajkbhi'),1)
        
    def test_7(self):
        self.assertEquals(CmpStr('jkshfiu1987491','jkshfiujskh19198'),-1)
        self.assertEquals(CmpStr('jafghi908','ja81074'),1)
        self.assertEquals(CmpStr('slhvoi108401','slhvoi10840100'),-1)
        self.assertEquals(CmpStr('alvhoqo91240','alvhoqo001984'),1)
        self.assertEquals(CmpStr('cbvi1984','cbvi0001984'),-1)
        self.assertEquals(CmpStr('nciuiq0009184791','nciuiq09184791'),1)
        self.assertEquals(CmpStr('zncj001874','zncj001874'),0)
        self.assertEquals(CmpStr('quryh98184','198401984quryhiquec'),-1)
        self.assertEquals(CmpStr('vwgbhoury198401','103480vwgbh'),1)
        self.assertEquals(CmpStr('zjhba90745','1074501zjhba'),1)
        self.assertEquals(CmpStr('19867fbja','1074501874fbjaniq'),-1)
        self.assertEquals(CmpStr('8741hjvbiw','1579hjv'),1)
        self.assertEquals(CmpStr('19765bviwyre','14710bviwyre'),0)
        
    def test_8(self):
        self.assertEquals(CmpStr('asdfghjklzxcvbnmqwertyuiopcvbqiugavbciquygfhcvbiagbchabscibasbhciqbfuabcuhasdcbiasbc','asdfghjklzxcvbnmqwertyuiopcvbqiugavbciquygfhcvbiagbchabscibasbhciqbfuabcuhasdcbi'),1)
        self.assertEquals(CmpStr('fhjbuqghfjhbvjhbfouqghodfighqgoihfhjvbajhfoquvjhbajhfgoqugfvbhjksbhakhfbghajhakbvfbava','fhjbuqghfjhbvjhbfouqghodfighqgoihfhjvbajhfoquvjhbajhfgoqugfvbhjksbhakhfbghajhakbvfbavajfhgbioa'),-1)
        self.assertEquals(CmpStr('jabvoqibhoifqhcjqhoiyruqiuvhqbwnvohqiwbhifhqoidhjskabncvhajbvfouqghfoqiihfioqhnvqhbgfuhqofhqofoqifasd','jabvoqibhoifqhcjqhoiyruqiuvhqbwnvohqiwbhifhqoidhjskabncvhajbvfouqghfoqiihfioqhnvqhbgfuhqofhqofoqifasd'),0)
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
        
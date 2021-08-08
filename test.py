import unittest
import functions

class TestAdd(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2.5,2.5)

    def test_false(self):
        self.assertNotEqual(2.5,2.5) 

    def test_type(self):
        self.assertEqual(type, type)

class Concatenate(unittest.TestCase):
    def test_equal(self):
          self.assertEqual(Gladys,Waithera)
    def test_false(self):
        self.assertNotEqual(Gladys, Waithera) 


if __name__ =='_main_':
    unittest.main()    




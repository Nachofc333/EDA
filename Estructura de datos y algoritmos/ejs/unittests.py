import unittest

def division_entera(a,b):
  return a/b

def isOdd(a):
    return a%2!=0

class Test(unittest.TestCase):

    def test_division_entera(self):
        self.assertEqual(division_entera(4,2), 2)

    def test_isOdd_1(self):
        self.assertEqual(isOdd(6), False)

    def test_isOdd_2(self):
        self.assertEqual(isOdd(7), True)

if __name__ == "__main__":
    unittest.main()
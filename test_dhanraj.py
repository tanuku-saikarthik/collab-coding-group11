import unittest
from main import function2

class TestFunction2(unittest.TestCase):

    def test_simple_palindromes(self):
        self.assertTrue(function2("madam"))
        self.assertTrue(function2("racecar"))
        self.assertTrue(function2("level"))
        self.assertTrue(function2("noon"))
        self.assertTrue(function2(""))

    def test_non_palindromes(self):
        self.assertFalse(function2("hello"))
        self.assertFalse(function2("python"))
        self.assertFalse(function2("openai"))
        self.assertFalse(function2("palindrome"))

    def test_case_insensitivity(self):
        self.assertTrue(function2("MadAm"))
        self.assertTrue(function2("RaceCar"))

    def test_space_insensitivity(self):
        self.assertTrue(function2("nurses run"))  # with space
        self.assertTrue(function2("step on no pets"))  # with spaces
        self.assertFalse(function2("this is not palindrome"))

    def test_numeric_palindromes(self):
        self.assertTrue(function2("12321"))
        self.assertTrue(function2("1221"))
        self.assertFalse(function2("12345"))

if __name__ == "__main__":
    unittest.main()

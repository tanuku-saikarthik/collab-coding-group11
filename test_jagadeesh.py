import unittest
from main import function1   # import your main file

class TestFunction1(unittest.TestCase):

    def test_reverse_word(self):
        self.assertEqual(function1("hello"), "olleh")

    def test_reverse_empty(self):
        self.assertEqual(function1(""), "")

    def test_reverse_sentence(self):
        self.assertEqual(function1("open ai"), "ia nepo")

    def test_reverse_palindrome(self):
        self.assertEqual(function1("madam"), "madam")

    def test_reverse_numbers(self):
        self.assertEqual(function1("12345"), "54321")


if __name__ == "__main__":
    unittest.main()

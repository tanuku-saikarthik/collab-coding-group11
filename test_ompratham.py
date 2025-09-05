import unittest
from main import function3

class TestVowelCount(unittest.TestCase):

    def test_vowel_count_basic(self):
        self.assertEqual(function3("hello"), 2)
        self.assertEqual(function3("world"), 1)
        self.assertEqual(function3("AEIOU"), 5)

    def test_vowel_count_empty(self):
        self.assertEqual(function3(""), 0)

    def test_vowel_count_no_vowels(self):
        self.assertEqual(function3("rhythm"), 0)

    def test_vowel_count_mixed(self):
        self.assertEqual(function3("Python Programming"), 4)
        self.assertEqual(function3("OpenAI"), 4)

if __name__ == "__main__":
    unittest.main()

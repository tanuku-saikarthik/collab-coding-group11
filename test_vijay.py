import unittest
from main import function4   

class TestFunction4(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(function4("issssn"), {'i': 1, 's': 4, 'n': 1})

    def test_empty_string(self):
        self.assertEqual(function4(""), {})

    def test_single_character(self):
        self.assertEqual(function4("a"), {'a': 1})

    def test_mixed_characters(self):
        self.assertEqual(function4("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_with_spaces(self):
        self.assertEqual(function4("a a"), {'a': 2, ' ': 1})

    def test_case_sensitivity(self):
        # Function should treat 'A' and 'a' as different
        self.assertEqual(function4("Aa"), {'A': 1, 'a': 1})

if __name__ == "__main__":
    unittest.main()

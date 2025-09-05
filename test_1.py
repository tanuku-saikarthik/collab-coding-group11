import unittest
from main import function1

class TestFunction1(unittest.TestCase):

    def test_reverse_simple(self):
        # Mock input() to return "hello"
        def mock_input(prompt=None):
            return "hello"
        original_input = __builtins__.input
        __builtins__.input = mock_input
        self.assertEqual(function1(), "olleh")
        __builtins__.input = original_input

    def test_reverse_empty(self):
        def mock_input(prompt=None):
            return ""
        original_input = __builtins__.input
        __builtins__.input = mock_input
        self.assertEqual(function1(), "")
        __builtins__.input = original_input

    def test_reverse_with_spaces(self):
        def mock_input(prompt=None):
            return "open ai"
        original_input = __builtins__.input
        __builtins__.input = mock_input
        self.assertEqual(function1(), "ia nepo")
        __builtins__.input = original_input


if __name__ == "__main__":
    unittest.main()

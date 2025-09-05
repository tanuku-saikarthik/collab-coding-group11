import unittest


def run_all_tests():

    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')


    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)


    if result.wasSuccessful():
        print("\n✅✅✅✅ ALL TESTS PASSED! 4 GREEN FLAGS ✅✅✅✅")
    else:
        print("\n❌ Some tests failed. Check the logs above.")

if __name__ == "__main__":
    run_all_tests()

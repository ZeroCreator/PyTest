# unit test case
import unittest


class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        firstValue = "geeks"
        secondValue = "geeksg"
        # error message in case if test case got failed
        message = "First value and second value are not unequal !"
        # assertNotEqual() to check unequality of first & second value
        self.assertNotEqual(firstValue, secondValue, message)


if __name__ == '__main__':
    unittest.main()

# unit test case
import unittest


class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_positive(self):
        firstValue = "geeks"
        secondValue = "geeks"
        # error message in case if test case got failed
        message = "First value and second value are not unequal !"
        # assertNotEqual() to check equality of first & second value
        self.assertNotEqual(firstValue, secondValue, message)


if __name__ == '__main__':
    unittest.main()
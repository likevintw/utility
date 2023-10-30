import unittest
import utility

# python3 -m unittest test_image_handler.py


class TestMethods(unittest.TestCase):

    def test_separate_by_space(self):
        result = utility.separate_by_space("hello world")
        assert result == ['hello', 'world']


if __name__ == '__main__':
    unittest.main()

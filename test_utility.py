import unittest
import utility

# python3 -m unittest test_utility.py


class TestMethods(unittest.TestCase):

    def test_replace_string_in_list(self):
        table = ['1.txt', '2.txt', '3.txt']
        result = utility.replace_string_in_list(table, '.txt', '.pdf')
        assert result == ['1.pdf', '2.pdf', '3.pdf']

        table = ['1.jpg', '2.jpg', '3.jpg']
        result = utility.replace_string_in_list(table, '.JPG', '.pdf')
        assert result == ['1.jpg', '2.jpg', '3.jpg']

    def test_separate_by_space(self):
        result = utility.separate_by_space("hello world")
        assert result == ['hello', 'world']

    def test_convert_dictionay_to_json(self):
        table = {'name': 'jay', 'age': '20'}
        result = utility.convert_dictionay_to_json(table)
        assert result == '{"name": "jay", "age": "20"}'

    def test_convert_json_to_dictionay(self):
        text = '{"name": "jay", "age": "20"}'
        result = utility.convert_json_to_dictionay(text)
        assert result['name'] == 'jay'


if __name__ == '__main__':
    unittest.main()

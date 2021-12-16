import unittest
from unittest.case import skip
import utility

# python3 -m unittest -v <.py>


class TestProcess(unittest.TestCase):

    def test_replace_string(self):
        data_list = []
        target = []
        replace = []
        want = []

        # 1.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("txt")
        replace.append("jpg")
        want.append(["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"])
        # 2.
        data_list.append(["Hello World"])
        target.append("World")
        replace.append("Good Morning")
        want.append(["Hello Good Morning"])

        for i in range(len(data_list)):
            result = utility.replace_string(
                data_list[i], target[i], replace[i])
            self.assertEqual(want[i], result)

    def test_remove_string(self):
        data_list = []
        target = []
        want = []

        # 1.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("txt")
        want.append([])
        # 2.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("2")
        want.append(["1.txt", "3.txt", "4.txt", "5.txt"])

        for i in range(len(data_list)):
            result = utility.remove_string(
                data_list[i], target[i])
            self.assertEqual(want[i], result)

    def test_keep_string(self):
        data_list = []
        target = []
        want = []

        # 1.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("txt")
        want.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        # 2.
        data_list.append(["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"])
        target.append("2")
        want.append(["2.txt"])

        for i in range(len(data_list)):
            result = utility.keep_string(
                data_list[i], target[i])
            self.assertEqual(want[i], result)

    def test_import_json(self):
        file_path = []
        want = []

        # 1.
        file_path.append("json.txt")
        want.append({'name': 'john', 'age': '50'})

        for i in range(len(file_path)):
            result = utility.import_json(file_path[i])
            self.assertEqual(want[i], result)

    def test_export_json(self):
        export_file_name = []
        data = []
        want = []

        # 1.
        export_file_name.append("export_json.txt")
        data.append({'name': 'Young', 'age': '44'})
        want.append({'name': 'Young', 'age': '44'})

        for i in range(len(export_file_name)):
            utility.export_json(export_file_name[i], data[i])
            result = utility.import_json(export_file_name[i])
            self.assertEqual(want[i], result)

    def test_save_as_log(self):
        pass

    def test_get_symbol_number_in_string(self):
        string = []
        symbol = []
        want = []

        # 1.
        string.append("123/234/134/134/2134")
        symbol.append("/")
        want.append(4)
        # 2.
        string.append("123/234/134/134/2134")
        symbol.append("1")
        want.append(4)
        # 3.
        string.append(
            r"/mnt/c/Users/LDS/Google 雲端硬碟/code_pool/python/module/utility")
        symbol.append("/")
        want.append(9)

        for i in range(len(string)):
            result = utility.get_symbol_number_in_string(string[i], symbol[i])
            self.assertEqual(want[i], result)

    def test_remove_last_slash(self):
        string = []
        want = []

        # 1.
        string.append("1/2/3/")
        want.append("1/2/3")
        # 2.
        string.append("1/2/3")
        want.append("1/2/3")
        # 3.
        string.append("1/2/3////////////")
        want.append("1/2/3")
        # 3.
        string.append("//////////")
        want.append("")
        # 4.
        string.append("/8/8/8/8//5//5///")
        want.append("/8/8/8/8//5//5")

        for i in range(len(string)):
            result = utility.remove_last_slash(string[i])
            self.assertEqual(want[i], result)

    def test_get_file_name_list(self):
        folder_path = []
        level_limitation = []
        want = []

        # 1.
        folder_path.append("test")
        level_limitation.append(5)
        want.append(['test/1/11.txt', 'test/2/22.txt'])
        # 2.
        folder_path.append("test/")
        level_limitation.append(5)
        want.append(['test/1/11.txt', 'test/2/22.txt'])

        for i in range(len(folder_path)):
            result = utility.get_file_name_list(
                folder_path[i], level_limitation[i])
            self.assertEqual(want[i], result)

    # @unittest.skip("")
    def test_get_file_path_list(self):
        folder_path = []
        level_limitation = []
        want = []

        # 1.
        folder_path.append("test")
        level_limitation.append(5)
        want.append(['test', 'test/1', 'test/2'])
        # 2.
        folder_path.append("test/")
        level_limitation.append(5)
        want.append(['test', 'test/1', 'test/2'])

        for i in range(len(folder_path)):
            result = utility.get_file_path_list(
                folder_path[i], level_limitation[i])
            self.assertEqual(want[i], result)
            

    def test_get_file_and_direct_path(self):
        folder_path = []
        level_limitation = []
        want_file = []
        want_direct = []

        # 1.
        folder_path.append("test")
        level_limitation.append(5)
        want_file.append(['test/1/11.txt', 'test/2/22.txt'])
        want_direct.append(['test', 'test/1', 'test/2'])
        # 2.
        folder_path.append("test/")
        level_limitation.append(5)
        want_file.append(['test/1/11.txt', 'test/2/22.txt'])
        want_direct.append(['test', 'test/1', 'test/2'])

        for i in range(len(folder_path)):
            file,direct = utility.get_file_and_direct_path(
                folder_path[i], level_limitation[i])
            self.assertEqual(want_file[i], file)
            self.assertEqual(want_direct[i], direct)


if __name__ == '__main__':
    unittest.main()

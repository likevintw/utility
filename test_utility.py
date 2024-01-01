import unittest
import utility

# python3 -m unittest -v test_utility.py


class TestMethods(unittest.TestCase):

    def test_convert_path_to_filename(self):
        path = "/Users/kevin/Downloads/stm32_pet_immune-master.zip"
        result = utility.convert_path_to_filename(path)
        assert (result=="stm32_pet_immune-master.zip")
    
    def test_get_file_birth_time(self):
        path = "./utility.py"
        float_time, str_time=utility.get_file_birth_time(path)
        assert(float_time==1703850105.4830298)
        assert(str_time=='20231229')

    
    def testget_file_last_updated_time(self):
        path = "./.gitignore"
        float_time, str_time=utility.get_file_last_updated_time(path)
        print(float_time, str_time)
        # assert(float_time==1703850548.8102973)
        # assert(str_time=='2023-12-29 19:49')


    def test_get_filepaths_in_a_folder(self):
        path = "../utility"
        dirs, files = utility.get_filepaths_in_a_folder(path)
        print(dirs)
        print(files)

    def test_get_all_filepaths_in_a_folder(self):
        path = "../utility"
        dir_path, dirs, files = utility.get_all_filepaths_in_a_folder(path)
        print(dir_path)
        print(dirs)
        print(files)

    @unittest.skip("not a good case")
    def test_get_all_filenames_in_a_folder(self):
        path = "/Users/kevin/Desktop/photo/"
        _, dirs, files = utility.get_all_filenames_in_a_folder(path)
        # print("dirs: ", dirs)
        # print("files: ", files)

    @unittest.skip("not a good case")
    def test_get_filenames_in_a_folder(self):
        path = "/Users/kevin/Desktop/photo/"
        dirs, files = utility.get_filenames_in_a_folder(path)
        # print("dirs: ", dirs)
        # print("files: ", files)

    @unittest.skip("not a good case")
    def test_replace_string_in_list(self):
        table = ['1.txt', '2.txt', '3.txt']
        result = utility.replace_string_in_list(table, '.txt', '.pdf')
        assert result == ['1.pdf', '2.pdf', '3.pdf']

        table = ['1.jpg', '2.jpg', '3.jpg']
        result = utility.replace_string_in_list(table, '.JPG', '.pdf')
        assert result == ['1.jpg', '2.jpg', '3.jpg']

    @unittest.skip("not a good case")
    def test_separate_by_space(self):
        result = utility.separate_by_space("hello world")
        assert result == ['hello', 'world']

    @unittest.skip("not a good case")
    def test_convert_dictionay_to_json(self):
        table = {'name': 'jay', 'age': '20'}
        result = utility.convert_dictionay_to_json(table)
        assert result == '{"name": "jay", "age": "20"}'

    @unittest.skip("not a good case")
    def test_convert_json_to_dictionay(self):
        text = '{"name": "jay", "age": "20"}'
        result = utility.convert_json_to_dictionay(text)
        assert result['name'] == 'jay'


if __name__ == '__main__':
    unittest.main()

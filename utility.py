
import json
import os
import string
from pypdf import PdfMerger

def remove_files(path, file_type):
    pass

def get_files_list(direct_path, ext):
    files = os.listdir(direct_path)
    # ext = ('.JPG', '.JEPG', '.jpg', '.jpeg')
    pdfs = []
    for file in files:
        if file.endswith(ext):
            pdfs.append(direct_path+file)
        else:
            continue
    return pdfs


def string_to_number(input):
    try:
        return float(input)
    except:
        print("Error")
        return None


def separate_by_space(txt):
    try:
        return txt.split()
    except:
        print("error")
        return None


def list_files_in_direct(direct_path) -> list:
    if not os.path.isdir(direct_path):
        print("direct {} is not exist".format(direct_path))
        return None
    try:
        result = os.listdir(direct_path)
        return result
    except:
        return None


def replace_string_in_list(data_list, target, replaced):
    result = []
    for i in data_list:
        buffer = i.replace(target, replaced)
        result.append(buffer)
    return result


def remove_string_in_list(data_list, target):
    result = []
    for i in data_list:
        if not target in i:
            result.append(i)
    return result


def keep_string_in_list(data_list, target):
    result = []
    for i in data_list:
        if target in i:
            result.append(i)
    return result


def import_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def export_json_file(export_file_name, data):
    with open(export_file_name, 'w') as file:
        json.dump(data, file)


def import_file(import_file_name):

    return_data = []

    if import_file_name == None:
        return None, "import_file_name is empty:{}".format(import_file_name)

    try:
        import_file = open(import_file_name, mode='r')
    except:
        return None, "open() error:{}".format(import_file_name)

    try:
        import_data = import_file.readlines()
    except:
        return None, "readlines() error:{}".format(import_file_name)

    for data in import_data:
        return_data.append(data.strip())

    return return_data


def export_file(file_path, data):
    with open(file_path, mode='w') as file:
        for i in data:
            file.write(i+"\n")


def get_symbol_number_in_string(string, symbol):
    if len(symbol) != 1:
        return "len(symbol) must be 1"
    numbers = 0
    for i in string:
        if i == "/" or i == "\ ":
            numbers += 1
    return numbers


def run_single_search(folder_path):
    file_path = []
    direct_path = []
    try:
        for file_name in os.listdir(folder_path):
            if os.path.isdir(folder_path+'/'+file_name):
                direct_path.append(folder_path+'/'+file_name)
            else:
                file_path.append(folder_path+'/'+file_name)
    except:
        print("The is no file in the {}".format(folder_path))
    finally:
        return file_path, direct_path


def remove_last_slash(string):
    while True:
        if len(string) == 0:
            break
        elif string[-1] == "/":
            string = string[:len(string)-1]
        else:
            break
    return string


def get_file_and_direct_path(folder_path) -> list:
    folder_path = remove_last_slash(folder_path)
    file_list = []
    direct_list = []

    data = os.walk(folder_path)

    for location, direct, file in data:
        if len(file) > 0:
            for j in file:
                file_list.append("{}/{}".format(location, j))
        direct_list.append(location)
    return file_list, direct_list


# def merge_pdfs(direct_path) -> bool:
#     pdfs = list_files_in_direct(direct_path)

#     handler = PdfMerger()

#     file_sequence = import_file(direct_path+'outline.txt')
#     if not len(file_sequence) == len(pdfs):
#         print("WARMING outline.txt is not the same with content")

#     try:
#         pdfs.sort()
#         pdfs.remove('.DS_Store')
#         pdfs.remove('outline.txt')
#         print(file_sequence)
#         for pdf in file_sequence:
#             print("read {}".format(pdf))
#             handler.append(direct_path+pdf)

#         name = direct_path+"result.pdf"
#         handler.write(name)
#         handler.close()
#         return True

#     except:
#         return False

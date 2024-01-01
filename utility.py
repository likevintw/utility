
import json
import os
import datetime


def convert_path_to_filename(path):
    results = path.split("/")
    return results[-1]


def get_file_created_time(path):
    established_time = os.path.getctime(path)
    timestamp_str = datetime.datetime.fromtimestamp(
        established_time).strftime('%Y-%m-%d %H:%M')
    return established_time, timestamp_str


def get_file_birth_time(path):
    established_time = os.stat(path).st_birthtime
    # timestamp_str = datetime.datetime.fromtimestamp(
    #     established_time).strftime('%Y-%m-%d %H:%M')
    timestamp_str = datetime.datetime.fromtimestamp(
        established_time).strftime('%Y%m%d')
    return established_time, timestamp_str


def get_filepaths_in_a_folder(path):
    dirs = []
    files = []
    results = os.listdir(path)
    for result in results:
        p = path+result
        if os.path.isdir(p):
            dirs.append(p+"/")
        else:
            files.append(p)
    return dirs, files


def get_all_filepaths_in_a_folder(folder_path):
    dirs = [folder_path]
    files = []
    while (len(dirs) > 0):
        path = dirs[0]
        dirs = dirs[1:]
        d, f = get_filepaths_in_a_folder(path)
        files += f
        dirs += d
    return folder_path, dirs, files


def get_filenames_in_a_folder(path):
    dirs = []
    files = []
    results = os.listdir(path)
    for result in results:
        if os.path.isdir(path+result):
            dirs.append(result)
        else:
            files.append(result)
    return dirs, files


def get_all_filenames_in_a_folder(folder_path):
    dirs = [""]
    files = []
    while (len(dirs) > 0):
        path = dirs[0]
        dirs = dirs[1:]
        d, f = get_filenames_in_a_folder(folder_path+path)
        files += f
        dirs += d
    return folder_path, dirs, files


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


def convert_json_to_dictionay(text) -> dict:
    return json.loads(text)


def convert_dictionay_to_json(dictionary) -> dict:
    return json.dumps(dictionary)

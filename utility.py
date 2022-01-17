
import json
import os


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

def import_file(file_path)->list:
    pass

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


def get_file_and_direct_path(folder_path, level_limitation) -> list:
    folder_path = remove_last_slash(folder_path)
    initial_slash_number = get_symbol_number_in_string(folder_path, "/")
    file_list = []
    direct_list = [folder_path]
    counter = 0
    while True:
        level = get_symbol_number_in_string(
            direct_list[counter], "/")-initial_slash_number
        if level > level_limitation:
            break
        f, d = run_single_search(direct_list[counter])
        file_list += f
        direct_list += d
        if counter >= len(direct_list)-1:
            break
        counter += 1

    return file_list, direct_list


def get_file_and_direct_path_walk(folder_path) -> list:
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

def export_python_function_name(file_path)->list:
    pass
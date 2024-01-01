import utility


def get_downloads_bith_time():
    path = "/Users/kevin/Downloads/"
    _, _, paths = utility.get_all_filepaths_in_a_folder(path)
    for p in paths:
        f = utility.convert_path_to_filename(p)
        _, time_str = utility.get_file_birth_time(p)
        print(f, time_str)


if __name__ == '__main__':
    get_downloads_bith_time()

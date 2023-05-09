import utility


if __name__ == '__main__':
    path = "/Users/kevin/Desktop/merge_pdfs/"
    if utility.merge_pdfs(path):
        print("merge pdfs successfully")
    else:
        print("fail to merge pdfs ")

from PIL import Image
import utility


if __name__ == '__main__':
    path = "/Users/kevin/Desktop/convert_jpg_to_pdf/"
    jpgs=utility.list_files_in_direct(path)
    jpgs.remove('.DS_Store')
    print(jpgs)
    for jpg in jpgs:
        image_1 = Image.open(path+jpg)
        im_1 = image_1.convert('RGB')
        filename=path+jpg[:-4]+'.pdf'
        im_1.save(filename)
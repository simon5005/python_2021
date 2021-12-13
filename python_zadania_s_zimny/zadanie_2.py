import os, os.path
from PIL import Image


def counter():
    files = os.listdir('.')
    count = 0
    for i in range(len(files)):
        if os.path.isfile(files[i]):
            count = count + 1
    print(count)



def files_print(loc):
    for element in os.listdir(loc):
        dir = os.path.join(loc, element)
        print(dir)
        if os.path.isdir(dir):
            files_print(dir)



def converter():
    for files in os.listdir('.'):
        if files.endswith(".jpg"):
            format_jpg = Image.open(files)
            format_png = format_jpg.save(files + '.png')



if __name__ == '__main__':
    #counter()
    #files_print('.')
    converter()
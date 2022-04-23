'''
traverse all subdirectories and files

'''
import os

file = os.getcwd()
print(f'{file}')
def listfile(file):
    with os.scandir(rf"{file}") as f:
        for item in f:
            if item.is_file:
                print(f'{item}')
            else:
                listfile(item)

listfile(file)

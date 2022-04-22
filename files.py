import os

def print_file(f):
    res = open(f).read() # we don't need with or close() when we use open(file).read() as a one-liner.
    if not res:
        print("[File is empty]")
    print(f'Readable: {open(f).readable()}')
    print(res)

path = "c:/Users/shailmis/Desktop/Python/google"
fname = "occurance.py"
os.chdir(path)
print(os.getcwd())
print_file(fname)

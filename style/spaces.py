"""This module is ran as a main to remove trailing spaces from a files.
"""
import os

def get_files_by_extension(extension, exclude=[]):
    files = []
    for d in os.listdir():
        if d.find(extension) > 0 and d[len(d)-3:len(d)] == extension and d not in exclude:
            files.append(d)
    return files

def trim_file(fname):
    file = []
    with open(fname, 'r') as fp:
        s = fp.readline()
        while s:
            if s[-1] == '\n':
                file.append(s[:-1].rstrip() + '\n')
            else:
                file.append(s.rstrip())
            s = fp.readline()
    with open(fname, 'w') as fp:
        for s in file:
            fp.write(s)

def trim_all_files(files):
    for file in files:
        print('triming %s'%(file))
        trim_file(file)

if __name__ == '__main__':
    files = get_files_by_extension('.py', exclude=['__init__.py', 'spaces.py'])
    trim_all_files(files)
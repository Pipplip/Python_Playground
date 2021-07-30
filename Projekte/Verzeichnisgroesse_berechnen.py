'''
Berechung der Größe eines Verzeichnisses
'''

import os
from tkinter import EXCEPTION

def get_dir_size(dir):
    sum = 0
    try:
        for i in os.scandir(dir):
            if i.is_file():
                sum += i.stat().st_size
            elif i.is_dir():
                sum += get_dir_size(i.path)
                
    except PermissionError:
        return 0
    except Exception:
        return 0

    return sum

def get_size(byte):
    for i in ["", "K", "M", "G", "T", "P"]:
        if byte < 1024:
            return f"{byte:.2f} {i}B"
        byte /= 1024
    return f"{byte:.2f} {i}EB"


size = get_dir_size(r"C:\Users\Philipp Becker\Desktop\Einführung in P")
print(get_size(size))
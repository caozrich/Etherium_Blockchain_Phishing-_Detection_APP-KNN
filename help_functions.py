import os
import sys

def is_cat(column): #check if the colum is categorical or not
    categorical_dtypes = ['object', 'category', 'bool']
    if column.dtype.name in categorical_dtypes:
        return True
    else:
        return False   
    


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

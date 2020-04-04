from tkinter import Tk
from tkinter.filedialog import askopenfilename

from typing import List,Tuple
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)

def file_dialog():
    Tk().withdraw()
    filename=askopenfilename()
    return filename
# file_dialog()

# with open(file_dialog()) as f:
#     print(f)

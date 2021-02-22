import os
from os.path import join
import sys
import math
import shutil
import tkinter
from tkinter import filedialog
from tkinter.constants import COMMAND
from tkinter.filedialog import askdirectory
from typing import Container
from PIL import Image, ImageTk
from pathlib import Path

# tkinter stuff
root = tkinter.Tk()

# window name
root.title("FileShift by Mobenator APPS")

# window size
frame = tkinter.Frame(root, height=300, width=600, bg='black')

root.mainloop
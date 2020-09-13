#Initial attempt at generating a dialog box prompting the user for unit SN.

import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog

ROOT = tk.Tk()

ROOT.withdraw()
# The input dialog

USER_INP = filedialog.askdirectory(title="Datasheet Review")

print(USER_INP)

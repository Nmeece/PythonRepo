#Initial attempt at generating a dialog box prompting the user for unit SN.

import tkinter as tk

from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# The input dialog

USER_INP = simpledialog.askstring(title="Datasheet Review", prompt="Please Enter a Serial Number:")

print(USER_INP)

'''
Nygel Meece
12AUG2020

This program utilizes tkinter dialog box to prompt a user for a string to search for in a predetermined location.
The results are returned in the console, where the number of string instances and the entire line the occur on are reported.
'''

import tkinter as tk                #Import tkinter - package for GUI things.
from tkinter import simpledialog
from tkinter import filedialog
import os

ROOT = tk.Tk()

ROOT.withdraw()
# The input dialog

USER_INP = simpledialog.askstring(title="Datasheet Review", prompt="Please Enter a Serial Number:")     #Use dialog box input to define variable "USER_INP". 'title' sets dailog box title. 'prompt' sets dialog messaage that precedes the input field. 

studentList = filedialog.askopenfilename(title= "Select a file")       # Opens a file browser dialog and copies the path from a user selected file

def CheckFail(studentList, string_in_file):                         #Search for the given string in file and return lines containing that sring, along with line numbers
    
    line_number     = 0                                             #Set 'line_number' variable and set initial value to 0. 
    results_list    = []                                            #Create list named "results_list"

    with open(studentList, 'r') as read_obj:                        #Open the file in read only mode and refer to it as 'read_obj'.        
        for line in read_obj:                                       #Read all lines in the file, one at a time and add 1 to variable "line_number".            
            line_number += 1                    
            if string_in_file in line:                              #Check each line for string. If yes, then add the line number & line as a tuple in the list.            
                results_list.append((line_number, line.rstrip()))

    return results_list                                             #Returns the list containing all mentions of the user defined string. 

fail_found = CheckFail(studentList, USER_INP)

print('Failures found: ', len(fail_found), '\nTest Number   ', 'Test Description   ', 'Min   ', 'Max   ', 'Actual   ', 'Pass/Fail   ', 'Date/Time')         #Print the the number of string instances found and categories for the data to follow.
for elem in fail_found:
    print('Line Number = ', elem[0], ':: Line = ', elem[1])                                                                                                 #Print the line where the string was found as well as the content of the line where the string was found.

#window = tk.Tk()

#label = window.Label(text=fail_found)

#label.pack()


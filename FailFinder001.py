from student import Student
#studentList = "C:/Users/nygel/PythonProjects/WorkRelated/StudentList.txt"
studentList = "/home/nmeece/Repo/PythonRepo/StudentList.txt"
def CheckFail(studentList, string_in_file):                         #Search for the given string in file and return lines containing that sring, along with line numbers
    
    line_number     = 0
    results_list    = []

    with open(studentList, 'r') as read_obj:                        #Open the file in read only mode and refer to it as 'read_obj'.        
        for line in read_obj:                                       #Read all lines in the file, one at a time and add 1 to variable "line_number".            
            line_number += 1                    
            if string_in_file in line:                              #Check each line for string. If yes, then add the line number & line as a tuple in the list.            
                results_list.append((line_number, line.rstrip()))

    return results_list

fail_found = CheckFail(studentList, 'Mechanical Eng.')

print('Failures found: ', len(fail_found), '\nTest Number', 'Test Description', 'Min', 'Max', 'Actual', 'Pass/Fail', 'Date/Time')
for elem in fail_found:
    print('Line Number = ', elem[0], ':: Line = ', elem[1])


## Alanna Whittington
## mod2_loops.py
## This program tests whether students are eligible for the Dean's List or Honor Roll.

while True:

    lastname = input("Enter students last name: ")
    if lastname == ("ZZZ"):
        print("Program has ended.")
        break
    else:
        firstname = input("Enter the student's first name: ")
        gpa = float(input("Input the student's GPA: "))
        if gpa >= 3.5:
            print(firstname,lastname,"has made the Dean's List.")
        if gpa >= 3.25:
            print(firstname,lastname,"has made the Honor Roll.")
        if gpa < 3.25:
            print(firstname,lastname,"has not made the Dean's List or Honor Roll.")
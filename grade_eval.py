#This is a simple program that takes the marks as input from the user and returns the Grade based on the marks
def grade(marks):
    if marks >=95:
        grade1='A'
    elif marks >=90 and marks <95:
        grade1='A+'
    elif marks <90:
        grade1='B'
    return grade1
m=int(input("Enter the marks : "))
print(grade(m))

name = input("Enter your name: ")
numberOfsubjects = int(input("Enter number of subjects: "))
subjects = []
marks = []
for subject in range(numberOfsubjects):
    subject_name = input(f"Enter subject name {subject + 1}: ")
    subjects.append(subject_name)
for number, subject in enumerate(subjects, start=1):
    print(f"{number} = {subject}")
marks = []
for subject in subjects:
    mark = float(input(f"Enter marks of {subject}: "))
    marks.append(mark)
for number, (subject, mark) in enumerate(zip(marks, subjects), start=1):
    print(f"{number}.  {subject} = {mark}")
total_marks = sum(marks)
import math
average = round(total_marks / numberOfsubjects, 2)
print("\nTOTAL MARKS = ", total_marks)
print("AVERAGE MARK = ", average)
for subject, mark in zip(subjects, marks):
    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "FAILED"
    print(f"\n{subject}: {mark} = {grade}")
    
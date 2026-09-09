for students in range(1, 3):
    name = input("Enter Student's name: ")
    Math = int(input("Enter maths Marks: "))
    science = int(input("Enter science Marks: "))
    sst = int(input("Enter SST Marks: "))
    english = int(input("Enter English Marks: "))
    total = Math + science + sst + english
    print(f"\nMATHS = {Math}\n  \nSCI = {science}\n \nSST = {sst}\n  \nENG = {english}\n \nTOTAL = {total}\n")


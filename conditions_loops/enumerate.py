############################################################
# Enumarate: Otomatik Counter/Indexer ile for loop
############################################################

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)



############################################################
# Döngüler (Loops)
############################################################

# for loop

students = ["John", "Mark", "Venessa", "Mariam"]


students[0]
students[1]
students[2]
students[3]


for  student in students:
    print(student.upper())


salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(int(salary * 20 / 100 + salary))

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

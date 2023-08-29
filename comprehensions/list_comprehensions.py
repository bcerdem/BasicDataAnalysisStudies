############################################################
# COMPREHENSIONS
############################################################

############################################################
# LIST COMPREHENSIONS
############################################################

# Birden fazla kod ve satır ile yapılabilecek işlemleri kolayca istediğimiz çıktı
# veri yapısına göre tek bir satırda gerçekleştirme imkanı sağlayan yapılardır.

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

###########################################################################

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper()  for student in students]

[student.upper() if student not in students_no else student.lower()  for student in students]
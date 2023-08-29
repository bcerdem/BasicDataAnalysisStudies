############################################################
# Uygulama - Mülakat Sorusu
############################################################

# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye yazınız.
# Tek indexte yer alan öğrencileri başka bir listeye yazınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Vanessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return print(groups)


st = divide_students(students)

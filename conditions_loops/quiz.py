students = ["Denise", "Arsen", "Tony", "Audrey"]

[student[0].upper() if len(student) % 2 != 0 else student[0].lower() for student in students]

string = "abracadabra"
group = []

for index, letter in enumerate(string, 1):
    if index * 2 % 2 == 0:
        group.append(letter)

print(group)

city_name = ["London", "Paris", "Berlin"]


def plate(cities):
    for index, city in enumerate(cities, 1):
        print(f"{index} : {city}")


plate(city_name)



wages = [10,20,30,40,50]

new_wages = []

for wage in wages:
    if wage < 40:
        new_w = wage * 1.10
        new_wages.append(new_w)
    else:
        new_wages.append(wage)

print(new_wages)

wages = [700, 800, 900, 1000]
[wage*1.1 if wage > 950 else wage * 1.2 for wage in wages]

students = ["Denise", "Arsen","Tony","Audrey"]

[student[0].upper() if len(student) % 2 != 0 else student[0].lower for student in students]

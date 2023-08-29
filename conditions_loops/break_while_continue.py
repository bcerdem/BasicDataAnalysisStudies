############################################################
# Break, While & Continue
############################################################

# Bir program akışında akışı kesmeye (break),
# ilgili şart gözlemlendiğinde o şartı atlayarak devam etmeye (continue),
# bir koşul sağlandığı sürece çalışmayı sürdümeye yarayan ifadelerdir (while)

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

for salary1 in salaries:
    if salary1 == 3000:
        continue
    print(salary1)

number = 1
while number < 5:
    print(number)
    number += 1
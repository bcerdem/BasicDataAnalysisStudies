############################################################
# Uygulama / Mülakat Sorusu
############################################################

# Amaç: Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Keyler orjinal değerler valueler ise değiştirilmiş değerler olacak.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2
for n in numbers if n % 2 == 0}

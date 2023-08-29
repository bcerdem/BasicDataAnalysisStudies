############################################################
# Koşullar (Conditions)
############################################################
# - Koşullar bir program yazımı esnasında, akış kontrolü sağlayan ve programların
# belirli kurallara göre ya da koşullara göre nasıl hareket etmesi gerektiğini
# kullanıcılar tarafından programlara bildirme imkanı sağlayan yapılardır.

# True - False
1 == 1
1 == 2

############################################################
# if
############################################################

if 1 == 1:
    print("Doğru")

if 1 == 2:
    print("Doğru")

number = 10

if number == 10:
    print("Number is 10")


    def number_check(number):
        if number == 10:
            print("Number is 10")

number_check(10)


############################################################
# Else & Elif
############################################################

def number_check(number):
    if number == 10:
        print("Number is 10")
    else:
        print("Number is not 10")


number_check(12)


def number_check(number):
    if number > 10:
        print("Greater than 10")
    elif number < 10:
        print("Less than 10")
    else:
        print("Equal 10")


number_check(1)

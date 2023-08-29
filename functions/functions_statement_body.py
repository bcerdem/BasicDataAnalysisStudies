############################################################
#  Fonksiyonların Statement/Body Bölümü
############################################################


# def function_name(parameters/arguments):
#               statements (function body)


def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")

    say_hi()


def multiplication(a, b):
    c = a * b
    print(c)

    multiplication(10, 9)


# Girilen iki sayıyı çarpıp bir liste içinde saklayacak fonsiyon

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

    add_element(18, 8)
    add_element(20 , 5)
    add_element(322 , 572*2)

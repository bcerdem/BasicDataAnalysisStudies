############################################################
#  Lokal & Global Değişkenler (Local & Global Variables)
############################################################

list_store = [1, 2]  # Global Variable


def add_element(a, b):
    c = a * b  # c = Local Variables
    list_store.append(c)
    print(list_store)


add_element(1, 9)
# Fonksiyonun içeriside bir değişken tanımlandıysa lokal değişken
# Fonksiyonun dışında bir değişken tanımlandıysa global değişken

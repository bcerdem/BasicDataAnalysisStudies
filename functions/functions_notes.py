############################################################
#  Ne Zaman Fonsiyon Yazma İhtiyacımız Olur?
############################################################

# Dont Repeat Yourself / DRY

def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)

calculate(98, 12, 78)

# Yapı olarak aynı işlemin yapılacağı durumlarda bir fonsiyon tanımlanır.
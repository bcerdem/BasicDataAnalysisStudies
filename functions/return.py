############################################################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
############################################################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78) * 10  # NonType fail


def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(98, 12, 78) * 10  # 14.102564...

a = calculate(98, 12, 78) * 10


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

varm, moisture, charge, output = calculate(98, 12, 78)
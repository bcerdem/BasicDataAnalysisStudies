########################################
# Sayılar (Numbers): int, float, complex
########################################

a = 5       # int
b = 10.5    # float
c = 2j+1    # complex

# Sayılar üzerinde matematiksel işlemler gerçekleştilebilir

a * 5
a * b / 10
# Bir sayının karesini almak için "**" ifadesi kullanılır

a ** 2

# sayıların ve operatörlerin arasında bir boşluk bırakılır. Bu PEP8 kurallarında geçerlidir
# PEP8; Python kod yapısının(boşluklar, girintiler vs.) nasıl olacağı üzerine yazılmış bir içeriktir.

####################
# Tipleri Değiştirme
####################

a = 5       # int
b = 10.5    # float

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)
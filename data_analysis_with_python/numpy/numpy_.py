############################################################
# Numpy / Numerical Python
############################################################

# - Neden Numpy? (Why Numpy) / Gelişmiş veri kütüphanesi
# - Numpy Array'i Oluşturmak (Creating Numpy Arrays)
# - Numpy Array Özellikleri (Attibutes of Numpy Arrays)
# - Yeniden Şekillendirme (Resharping)
# - Index Seçimi (Index Selection)
# - Slicing
# - Fancy Index
# - Numpy'da Koşullu İşlemler (Conditions on Numpy)
# - Matematiksel İşlemler (Mathematical Operations)


# - Neden Numpy? (Why Numpy)
# Numerical işlemler için geliştirilmiş bir kütüphanedir
# Hız - Sabit tipte veri tutarak gerçekleştiriyor
# Vektörel seviyede işlemler yapmayı sağlıyor(Daha az çabayla daha fazla işlem yapmayı sağlıyor)


import numpy_ as np
a = [1,2,3,4]
b = [2,3,4,5]


ab = []

for i in range(0,len(a)):
    ab.append(a[i] * b[i])


#numpy

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a * b




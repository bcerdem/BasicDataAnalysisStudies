############################################################
# Sözlük (Dictionary)
############################################################

# - Değiştirilebilir.
# - Sırasızdır. (3.7'den sonra sıralı)
# - Kapsayıcıdır.

# key -value

dictionary = {
    "REG": "Regression",
    "LOG": "Logistic Regression",
    "CART": "Classification and Reg"}
# Dictionary'lerde key'i çağırdığınızda value gelir.

dictionary["REG"] #Regression

############################################################
# Key Sorgulama
############################################################

"REG" in dictionary #True
"BES" in dictionary #False

############################################################
#  Value Değiştirme
############################################################

dictionary["REG"] = ["Regression1"]

############################################################
# Tüm Key'lere Erişmek
############################################################

dictionary.keys()

############################################################
# Tüm Value'lere Erişmek
############################################################

dictionary.values()

############################################################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
############################################################

dictionary.items()

############################################################
# Key - Value Değerlerini Güncellemek
############################################################

dictionary.update({"REG": 11})

dictionary.update({"RF": 10})

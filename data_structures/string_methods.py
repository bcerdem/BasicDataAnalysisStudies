############################################################
# String (Karakter Dizisi) Metodları
############################################################

# Method: Çeşitli görevleri yerine getiren fonksiyon benzeri yapılardır.
# Sınıflar (class) içerisinde tanımlanan fonksiyonlardır

#Kullanılabilecek methodları listelemek için;
dir(int)
dir(str)

############################################################
# len /  string uzunluğu
############################################################

name = "Besimcan"
type(name)
len(name)

# Kullanılan bir yapının Method ya da Fonksiyon olup olmadığını;
#Eğer bir fonksiyon class yapısı içerisinde tanımlandıysa Method,
#Eğer bir fonksiyon class yapısı içerisinde tanımlanmadıyda Fonksiyondur.


############################################################
# upper() & lower(): küçük büyük dönüşümleri
############################################################

"name".upper() # NAME
"NAME".lower() # name

############################################################
# replace: Karakter değiştirme
############################################################

b = "Besim can Erdem"
b.replace("Besim can","Besimcan")

############################################################
# split: Kelimeyi, Cümleyi böler
############################################################

b = "Besimcan ERDEM"
b.split()

############################################################
# strip: Kelimeyi, Cümleyi kırpar
############################################################

" Besimcan ".strip()
"Besimcan".strip("B")

############################################################
# capitalize: İlk harfleri büyütmek için kullanılır.
############################################################

"besimcan Erdem".capitalize()

# Methodlara " dir(str) " şeklinde ulaşılabilinir.

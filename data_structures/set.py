############################################################
#  Set
############################################################

# - Değiştirilebilir.
# - Sırasızdır + Eşsizdir
# - Kapsayıcıdır.

############################################################
#  difference(): İki Kümenin Farkı
############################################################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2
# set2'de olup set1'de olmayanlar
set2.difference(set1)
set2 - set1
############################################################
# symetric_difference(): İki kümede de birbirlerine göre olmayanlar
############################################################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

############################################################
# intersection(): İki kümenin kesişimi
############################################################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)
set1 & set2

############################################################
# unıon(): İki kümenin birleşimi
############################################################

set1.union(set2)
set2.union(set1)

############################################################
# isdisjoint(): İki kümenin kesişimi boş mu?
############################################################

set1.isdisjoint(set2)
set2.isdisjoint(set1)

############################################################
# issubset(): Bir Küme Diğer kümenin alt kümesi mi?
############################################################

set1.issubset(set2)
set2.issubset(set2)

############################################################
# issuperset(): Bir küme diğer kümeyş kapsıyor mu?
############################################################

set1.issuperset(set2)
set2.issuperset(set2)

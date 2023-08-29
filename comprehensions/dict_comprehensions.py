############################################################
# DICT COMPREHENSIONS
############################################################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys() # keyleri verir
dictionary.values() # value değerlerini verir
dictionary.items() # tablo olarak görmek için


{k : v ** 2 for (k,v) in dictionary.items()}

{k.upper(): v *2 for (k,v) in dictionary.items()}

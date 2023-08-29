############################################################
# Uygulama - Mülakat Sorusu
############################################################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHN aNd i aM LeArNiNg pYtHoN"


str = "hi my name is john and i am learning python"


def altenating(str):
    new_string = ""
    # Girilen string'in index'lerinde gez.
    for string_index in range(len(str)):
        #index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += str[string_index].upper()
            # index tek ise küçük harfe çevir.
        else:
            new_string += str[string_index].lower()
    print(new_string)

altenating(str)

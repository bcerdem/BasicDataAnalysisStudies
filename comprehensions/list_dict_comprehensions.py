############################################################
# LIST/DICT COMPREHENSIONS
############################################################

############################################################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek / APP 1
############################################################

# Before
# ['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_looses','abbrev']
# After
# ['TOTAL','SPEEDING','ALCOHOL','NOT_DISTRACTED','NO_PREVIOUS','INS_PREMIUM','INS_LOOSES','ABBREV']


import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

A = [ ]

for col in df.columns:
    A.append(col.upper())

df.columns = [col.upper() for col in df.columns]


############################################################
# İsminde "INS"  olan değişkenlerin başına "FLAG" diğerlerine "NO_FLAG" eklemek istiyoruz / APP 2
############################################################

# Before
# ['TOTAL','SPEEDING','ALCOHOL','NOT_DISTRACTED','NO_PREVIOUS','INS_PREMIUM','INS_LOOSES','ABBREV'

# After
# ['NO_FLAG_TOTAL','NO_FLAG_SPEEDING','NO_FLAG_ALCOHOL','NO_FLAG_NOT_DISTRACTED','NO_FLAG_NO_PREVIOUS','FLAG_INS_PREMIUM','FLAG_INS_LOOSES','NO_FLAG_ABBREV']


[col for col in df.columns if "INS" in col]

["FLAG_"+ col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_"+ col for col in df.columns]

############################################################
# İsminde "INS"  olan değişkenlerin başına "FLAG" diğerlerine "NO_FLAG" eklemek istiyoruz / APP 2
############################################################

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_"+ col for col in df.columns]


############################################################
# Amaç Key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak / APP 3
# Sadece sayısal değişkenler için yapılacak
############################################################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
# 'speeding': ['mean', 'min', 'max', 'var'],
# 'alcohol': ['mean', 'min', 'max', 'var'],
# 'not_distracted': ['mean', 'min', 'max', 'var'],
# 'no_previous': ['mean', 'min', 'max', 'var'],
# 'ins_premium': ['mean', 'min', 'max', 'var'],
# 'ins_looses': ['mean', 'min', 'max', 'var'],
# 'abbrev': ['mean', 'min', 'max', 'var']}

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "0"]

soz = {}
agg_list = ['mean', 'min', 'max', 'var']


for col in num_cols:
    soz[col] = agg_list


# Kısayol

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)
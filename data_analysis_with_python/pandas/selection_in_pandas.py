############################################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
############################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head(10)

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# Silmek için
# df = df.drop(delete_indexes, axis=0).head(10)
# df.drop(delete_indexes, axis=0, inplace=True)

############################################################
# Değişkeni Indexe Çevirmek

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1, inplace=True)


############################################################
# Indexi Değişkene Çevirmek

df.index

df["age"] = df.index

df.head()


df = df.reset_index().head()


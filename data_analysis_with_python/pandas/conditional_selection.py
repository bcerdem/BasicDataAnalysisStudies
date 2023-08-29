############################################################
# Koşullu Seçim İşlemleri (Conditional Selection)
############################################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# 50 yaşından büyükleri sorgulama
df[ df[ "age" ] > 50 ].head()
# 50 yaşından büyüklerin sayısı
df[ df[ "age" ] > 50 ][ "age" ].count()
# tek bir kolon seçme
df.loc[ df[ "age" ] > 50, "class" ].head()
# iki tane kolon seçme
df.loc[ df[ "age" ] > 50, [ "age", "class" ] ].head()
# birden fazla koşul giriliyorsa koşulların parantez içine alınması gerekmektedir.
df.loc[ (df[ "age" ] > 50) & (df[ "sex" ] == "male"), [ "age", "class", "sex" ] ].head()

# examples // "|" sembolü "yada" seçimi yapmak için kullanılır
df_new = df.loc[ (df[ "age" ] > 50)
        & (df[ "sex" ] == "male")
        & ((df[ "embark_town" ] == "Cherbourg" )| (df["embark_town"] == "Southampton")),
[ "age", "class", "sex", "embark_town" ] ].head()


df_new
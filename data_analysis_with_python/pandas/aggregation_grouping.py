############################################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
############################################################

# - count() = sayma işlemi
# - first() = ilk değer
# - last() = son değer
# - mean() = ortalaması
# - median()
# - min() = en düşük
# - max() = en yüksek
# - std()
# - var()
# - sum()
# - group by işleminden sonra yukarıdakiler kullanılabiliyor. - #
# - pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# Cinsiyete göre yaş ortalaması;
df.groupby("sex")["age"].mean()
# Yaşların toplamı ve cinsiyete göre yaş ortalaması;
df.groupby("sex").agg({"age": ["mean","sum"]})
# İki tane değişken kullanmak;
df.groupby("sex").agg({"age": ["mean","sum"],
                       "embark_town": ["count"]})
# neden pivot table'a ihtiyacımız var;
df.groupby("sex").agg({"age": ["mean","sum"],
                       "survived": ["mean"]}) # gemiye binen kadınarın %74'ü hayatta kalmış, Erkeklerin %18'i hayatta kalmış
# Başka kategorik değişkenlere göre kırılım;
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                        "survived": ["mean"]})
# Başka boyut ekleme;
df.groupby(["sex", "embark_town","pclass"]).agg({"age": ["mean"],
                                        "survived": ["mean"]})
# frekans bilgisi ekleme;
df.groupby(["sex", "embark_town","pclass"]).agg({"age": ["mean"],
                                        "survived": ["mean"],"sex":["count"]})
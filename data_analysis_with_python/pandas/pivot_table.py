############################################################
# Pivot Table
############################################################
# Pivot table: Group by işlemlerine benzer şekilde veri setlerini kırılımlar
# açısından değerlendirmek ve ilgilendiğimiz özel istatistiği bu kırılımlar
# açısından görme imkanı sağlar.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()
# Pivot table girilen hücrelerin ön tanımlı olarak ortalamasını alır.
df.pivot_table("survived","sex","embarked")
# İstenidiği taktirde aggfunc="" ile başka bir aggrigate function girilebilir.
df.pivot_table("survived","sex","embarked",aggfunc= "std")
# Daha fazla boyut bilgisi ekleme;
df.pivot_table("survived","sex",["embarked","class"])
# Sayısal değişkeni kategorik değişkene çevirmek;
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40 ,90])
# Eğer sayısal değerin içeriği biliniyorsa pd.cut(), bilinmiyorsa pd.qcut() kullanılabilir.
df.pivot_table("survived","sex",["new_age", "class"])

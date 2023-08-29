############################################################
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN
############################################################

############################################################
# MATPLOTLIB
############################################################

### Kategorik değişken: Sütun Grafik ile göreselleştirilir.
# seahorn: countplot / matlablib: bar

### Sayısal değişken: hist, boxplot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar')
plt.show()
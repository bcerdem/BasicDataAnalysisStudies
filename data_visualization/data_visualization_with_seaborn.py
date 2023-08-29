############################################################
# Seaborn ile Veri Görselleştirme (Data Visualization with Seaborn)
############################################################
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
##########################################
# Kategorik Değişken Göreselleştirme
##########################################
df["sex"].value_counts()
sns.countplot(x=df["sex"],data=df)
plt.show()
##########################################
# Sayısal Değişken Göreselleştirme
##########################################
# boxplot
sns.boxplot(x = df["total_bill"])
plt.show()
# hist
df["total_bill"].hist()
plt.show()
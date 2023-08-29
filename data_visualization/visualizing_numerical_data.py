############################################################
# Sayısal Değişken Görselleştirme
############################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

#hist
plt.hist(df["age"])
plt.show()

#box
plt.boxplot(df["fare"])
plt.show()
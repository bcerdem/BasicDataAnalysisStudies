############################################################
# Değişkenler Üzerinde İşlemler
############################################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")

df.head()

"age" in df
df["age"].head()
df.age.head()

type(df["age"].head()) #pandas.core.series.Series
type(df[["age"]].head())#pandas.core.frame.DataFrame

df[["age","alive"]]

col_names = ["age", "adult_male","alive"]
df[col_names]


df["age2"] = df["age"] **2


df.drop("age2", axis=1).head()

df.drop(col_names , axis=1).head()


df.loc[:, ~df.columns.str.contains("age")].head()
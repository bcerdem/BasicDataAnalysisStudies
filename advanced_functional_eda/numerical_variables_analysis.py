###################################################
# Sayısal Değişken Analizi (Analysis of Numerical Variables)
###################################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")

df[["age","fare"]].describe().T

cat_cols = [ col for col in df.columns if str(df[ col ].dtypes) in [ "category", "object", "bool" ] ]
num_bat_cat = [ col for col in df.columns if df[ col ].nunique() < 10 and df[ col ].dtypes in [ "int64", "float" ] ]
cat_but_car = [ col for col in df.columns if df[ col ].nunique() > 20 and df[ col ].dtypes in [ "category", "object" ] ]
cat_cols = cat_cols + num_bat_cat

num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float"]]

num_cols = [col for col in df.columns if col not in cat_cols]

def num_summary(dataframe, numerical_col,plot= False):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95,0.99]
    print(dataframe[numerical_col].describe().T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col,plot=True)
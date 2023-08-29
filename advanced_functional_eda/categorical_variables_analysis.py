############################################################
# Kategorik Değişken Analizi (Analysis of Categorical Variables)
############################################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

cat_cols = [ col for col in df.columns if str(df[ col ].dtypes) in [ "category", "object", "bool" ] ]

num_bat_cat = [ col for col in df.columns if df[ col ].nunique() < 10 and df[ col ].dtypes in [ "int64", "float" ] ]

cat_but_car = [ col for col in df.columns if df[ col ].nunique() > 20 and df[ col ].dtypes in [ "category", "object" ] ]

cat_cols = cat_cols + num_bat_cat


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[ col_name ].value_counts(),
                        "Ratio": 100 * dataframe[ col_name ].value_counts() / len(dataframe)}))
    print("############################################")

    if plot:
        sns.countplot(x=dataframe[ col_name ], data=dataframe)
        plt.show(block=True)


for col in cat_cols:
    if df[ col ].dtypes == "bool":
        df[ col ] = df[ col ].astype(int)
    else:
        cat_summary(df, col, plot=True)

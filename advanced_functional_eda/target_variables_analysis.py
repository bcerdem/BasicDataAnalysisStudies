############################################################
# Hedef Değişlem Analizi (Analysis of Target Variables)
############################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)



def grap_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişlenlerini verir.
    Parameters
    ----------
    dataframe: dataframe
            değişken isimleri alınmak istenen dataframe'dir
    cat_th: int, float
            numerik fakat kategorik olan değişkenler için sınıf eşiği değeri
    car_th: int, float
            kategorik fakat kardinal değişkenler için sınıf eşiği değeri

    Returns
    -------
    cat_cols: list
            Kategorik değişken listesi
    num_cols: list
            Numerik değişken listesi
    cat_but_car: list
            Kategorik görünümlü kardinal değişken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat, cat_cols'un içerisinde.

    """
    cat_cols = [ col for col in df.columns if str(df[ col ].dtypes) in [ "category", "object", "bool" ] ]
    num_bat_cat = [ col for col in df.columns if df[ col ].nunique() < 10 and df[ col ].dtypes in [ "int64", "float" ] ]
    cat_but_car = [ col for col in df.columns if
                    df[ col ].nunique() > 20 and df[ col ].dtypes in [ "category", "object" ] ]
    cat_cols = cat_cols + num_bat_cat
    cat_cols = [ col for col in cat_cols if col not in cat_but_car ]

    num_cols = [ col for col in df.columns if df[ col ].dtypes in [ "int64", "float" ] ]
    num_cols = [ col for col in df.columns if col not in cat_cols ]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_bu_cat: {len(num_bat_cat)}")

    return  cat_cols,num_cols, cat_but_car

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[ col_name ].value_counts(),
                        "Ratio": 100 * dataframe[ col_name ].value_counts() / len(dataframe)}))
    print("############################################")

    if plot:
        sns.countplot(x=dataframe[ col_name ], data=dataframe)
        plt.show(block=True)

cat_cols, num_cols, cat_but_car = grap_col_names(df)


cat_summary(df,"survived")


###################################################
# Hedef değişkenin Kategorik değişkenler ile analizi
###################################################

df.groupby("sex")["survived"].mean()

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")

target_summary_with_cat(df,"survived","pclass")


for col in cat_cols:
    target_summary_with_cat(df,"survived",col)



###################################################
# Hedef Değişkenin Sayısal Değişkenler ile Analizi
###################################################


df.groupby("survived")["age"].mean()

df.groupby("survived").agg({"age":"mean"})

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


target_summary_with_num(df, "survived","age")

for col in num_cols:
    target_summary_with_num(df, "survived", col)
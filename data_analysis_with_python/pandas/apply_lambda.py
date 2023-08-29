############################################################
# Apply & Lambda
############################################################
import pandas as pd
import  seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# Apply: Satır ya da sütünlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar
# Lambda: Bir fonksiyon tanımlama şeklidir. Fakat kullan at fonksiyondur. Yani kod akışı esnasında bir kez kullanılır.

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

#Klasik Yöntem
(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

# Apply & Lamda

df[["age","age2","age3"]].apply(lambda x: x/10).head()

# Programatik

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

# Complex
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean())/ x.std()).head()

# More Complex

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# Değişkene atama;

# df.loc[:, ['age','age2','age3']] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.head()
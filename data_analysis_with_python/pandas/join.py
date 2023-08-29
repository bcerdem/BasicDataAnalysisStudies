############################################################
# Birleştirme (Join) İşlemleri
############################################################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

############################################################
# Concat (Basit)
pd.concat([df1,df2])

#Indexleri 0'lamadan kullanmak için;

pd.concat([df1, df2], ignore_index=True)

############################################################
# Merge (Detaylı)

df1 = pd.DataFrame({
    'employees': ["John", 'Dennis', "Mark", "Maria"],
    'group': ["accounting", "engineering", "engineering", "hr"]
})

df2 = pd.DataFrame({
    "employees": ["Mark", "John", "Dennis", "Maria"],
    "start_date": [2010, 2009, 2014, 2019]
})

# Değişkeni belirlemeden;
pd.merge(df1,df2)
# Değişkeni belirlleyip;
pd.merge(df1,df2, on="employees")

# Amaç: Her çalışanın müdür bilgisine erişilmek isteniyor

df3 = pd.merge(df1,df2)

df4 = pd.DataFrame({
    "group": ["accounting","engineering","hr"],
    "manager": ["Besim", "Can", "Erdem"]
})

pd.merge(df3,df4)
# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki,
# numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# Numeric olmayan değişkenlerin isimleri de büyümeli

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

new_columns = [ f"NUM_{col.upper()}" if pd.api.types.is_numeric_dtype(df[ col ]) else col.upper() for col in
                df.columns ]

print(new_columns)

# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "_FLAG" yazınız. Tüm değişkenlerin isimleri büyük harf olacak

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

new_columns = [ col.upper() + "_FLAG" if "no" not in col else col for col in df.columns ]

print(new_columns)

# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan,
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

og_list = [ "abbrev", "no_previous" ]

import seaborn as sns

df = sns.load_dataset("car_crashes")

og_list = [ "abbrev", "no_previous" ]

# Og_list içinde yer almayan değişken isimlerini new_cols listesine ekleyelim
new_cols = [ col for col in df.columns if col not in og_list ]

# Yeni DataFrame'i seçtiğimiz sütunlarla oluşturalım
new_df = df[ new_cols ]

print(new_df)

##############################################################################################
# Pandas Alıştırmaları

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız. +
# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
# Görev 12: who değişkenini dataframe’den çıkarınız.
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
# setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

import pandas as pd
import seaborn as sns

# Görev 1;
df = sns.load_dataset("titanic")
df.head()
# Görev 2;
df.groupby("sex").count()
# Görev 3;
for col in df.columns:
    unique_values = df[ col ].unique()
    print(f"Unique values for {col}: {unique_values}")
# Görev 4;
for col in [ "pclass", "parch" ]:
    unique_values_count = df[ col ].unique().count()
    print(f"Unique values count for {col}: {unique_values_count}")
# Görev 5;
unique_pclass_count = df[ 'pclass' ].nunique()
unique_parch_count = df[ 'parch' ].nunique()

print(f"Unique values count for pclass: {unique_pclass_count}")
print(f"Unique values count for parch: {unique_parch_count}")
# Görev 6
# embarked değişkeninin tipini kontrol edelim
print("Before:", df[ 'embarked' ].dtype)

# embarked değişkeninin tipini category olarak değiştir
df[ 'embarked' ] = df[ 'embarked' ].astype('category')

# tekrar tipini kontrol et
print("After:", df[ 'embarked' ].dtype)
# Görev 7;
embarked_c = df[ df[ 'embarked' ] == 'C' ]
print(embarked_c)
# Görev 8;
embarked_not_s = df[ df[ 'embarked' ] != 'S' ]
print(embarked_not_s)

# Görev 9;
young_female_passengers = df[ (df[ 'age' ] < 30) & (df[ 'sex' ] == 'female') ]
print(young_female_passengers)

# Görev 10;
high_fare_or_old_age_passengers = df[ (df[ 'fare' ] > 500) | (df[ 'age' ] > 70) ]
print(high_fare_or_old_age_passengers)

# Görev 11;
missing_values_sum = df.isnull().sum()
print(missing_values_sum)

# Görev 12;
df.drop(columns='who', inplace=True)

# Görev 13;
df.drop(columns='who', inplace=True)

# Görev 14;
age_median = df[ 'age' ].median()
df[ 'age' ].fillna(age_median, inplace=True)
# Görev 15;
survived_statistics = df.groupby([ 'pclass', 'sex' ])[ 'survived' ].agg([ 'sum', 'count', 'mean' ])
print(survived_statistics)


# Görev 16;
def age_flag(age):
    if age < 30:
        return 1
    else:
        return 0


df[ 'age_flag' ] = df[ 'age' ].apply(age_flag)

# Görev 17;
tips_data = sns.load_dataset("tips")

# Görev 18;
tips_data = sns.load_dataset("tips")
time_total_bill_stats = tips_data.groupby('time')[ 'total_bill' ].agg([ 'sum', 'min', 'max', 'mean' ])
print(time_total_bill_stats)

# Görev 19;
tips_data = sns.load_dataset("tips")
day_time_total_bill_stats = tips_data.groupby([ 'day', 'time' ])[ 'total_bill' ].agg([ 'sum', 'min', 'max', 'mean' ])
print(day_time_total_bill_stats)

# Görev 20;
tips_data = sns.load_dataset("tips")
lunch_female_stats = tips_data[ (tips_data[ 'time' ] == 'Lunch') & (tips_data[ 'sex' ] == 'Female') ].groupby('day')[
    'total_bill', 'tip' ].agg([ 'sum', 'min', 'max', 'mean' ])
print(lunch_female_stats)

# Görev 21;
tips_data = sns.load_dataset("tips")
average_for_conditions = tips_data.loc[
    (tips_data[ 'size' ] < 3) & (tips_data[ 'total_bill' ] > 10), 'total_bill' ].mean()
print(average_for_conditions)

# Görev 22;
tips_data = sns.load_dataset("tips")
tips_data[ 'total_bill_tip_sum' ] = tips_data[ 'total_bill' ] + tips_data[ 'tip' ]

# Görev 23;
tips_data = sns.load_dataset("tips")
sorted_top_30 = tips_data.sort_values(by='total_bill_tip_sum', ascending=False).head(30).copy()

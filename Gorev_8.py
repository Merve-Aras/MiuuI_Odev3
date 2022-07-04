# GÖREV-8 List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini
# seçiniz ve yeni bir data frame oluşturunuz.

og_list = ["abbrev", "no_previous"]

import seaborn as sns
df = sns.load_dataset("car_crashes")

df2 = set(df)

liste = set(og_list)

print(df2.symmetric_difference(liste))
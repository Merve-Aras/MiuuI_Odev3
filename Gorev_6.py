# GÖREV-6 List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çevir
# ve başına NUM ekleyiniz.

import seaborn as sns

df = sns.load_dataset("car_crashes")
print(df.columns)

sutun_adi = df.columns

for sutun in df.columns:
    if df[sutun].dtype != "O":
        print("NUM_" + sutun.upper())



















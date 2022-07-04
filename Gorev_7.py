# GÖREV-7 List Comprehension yapısı kullanarak car_crashes verisinde isminde"no" barındırmayan değişkenlerin isimlerinin
# sonuna "FLAG" yazınız.

import seaborn as sns

df = sns.load_dataset("car_crashes")
print(df.columns)

new_columns = [col + "_FLAG" for col in df.columns if "no" not in col]

print(new_columns)
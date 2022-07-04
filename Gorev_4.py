# GÖREV-4 Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
# dict={ "Christian" : ["America",18],
#       "Daisy": ["England",12],
#       "Antonio": ["Spain",22],
#       "Dante": ["İtaly",25]}
# Adım1: Key değerlerine erişiniz.
# Adım2: Value'lara erişiniz.
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım5: Antonio'yu dictionary'den siliniz.

sozluk = { "Christian" : ["America",18],
        "Daisy": ["England",12],
        "Antonio": ["Spain",22],
        "Dante": ["İtaly",25]}


print(sozluk.keys())
print(sozluk.values())

sozluk["Daisy"] = ["England",13]
print(sozluk)

sozluk["Ahmet"] = ["Turkey", 24]
print(sozluk)

sozluk.pop("Antonio")
print(sozluk)








# GÖREV-3 Verilen listeye aşağıdaki adımları uygulayınız.
liste= ["D","A","T","A","S","C","İ","E","N","C","E",]
# Adım1: Verilen listenin eleman sayısına bakınız.
# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım4: Sekizinci indeksteki elemanı siliniz.
# Adım5: Yeni bir eleman ekleyiniz.
# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.


print("uzunluk: {0}".format(len(liste)))

print(liste[0], liste[10])

new_list = liste[:4]
print(new_list)

liste.pop(8)
print(liste)

liste.append("***")
print(liste)

liste.insert(8,"N")
print(liste)
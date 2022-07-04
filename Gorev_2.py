# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız

# text = "The goal is to turn data into information, and information into insignt."


def big_letter(text):
    a = text.upper()
    b = a.replace(","," ")
    c = b.replace(".", " ")
    d = c.split()
    print(d)


big_letter("The goal is to turn data into information, and information into insight.")



"""
print(text.upper())
print(text.replace("," , " "))
print(text.replace("." , " "))
print(text.split())
"""
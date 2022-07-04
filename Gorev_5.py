# GÖREV-5 Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan
# ve bu listeleri return eden fonksiyon yazınız.

l = [2,13,18,93,22]

def tek_cift (liste):
    tek = []
    cift = []
    for i in liste:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    print(tek,cift)
    return tek, cift

tek_cift(l)
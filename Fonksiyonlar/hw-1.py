# Problem 1
# 1'den 1000'e kadar olan sayılardan mükemmel -->prosedurde yok 
# sayı olanları ekrana yazınız
# Bunun için bir sayının mükemmel 
# olup olmadığını dönen bir tane fonksiyon yazın.

# Bir sayının bölenlerinin toplamı 
# kendine eşitse bu sayı mükemmel bir sayıdır.
#  Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).


def muk(sayi):
    top=0
    for i in range(1,sayi):
       if sayi%i==0:
            top=+1
    return sayi==top



for i in range(1,1001):
    if muk(i):
        print("mukemmel",i)

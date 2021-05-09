# Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. 
# Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. 
# Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın
# . Daha sonra, içinde çift ve tek sayılar bulunduran bir 
# liste tanımlayın ve liste üzerinde 
# gezinerek ekrana sadece çift sayıları bastırın.

def cift(a):
    if a%2==0:
        return a
    else:
        raise ValueError


liste=[1,2,3,4]

for i in liste:  #Listede gezinmek :D
    try:
        print(cift(i))
    except ValueError:
        pass
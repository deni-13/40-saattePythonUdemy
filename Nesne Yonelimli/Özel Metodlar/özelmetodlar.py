"""class Kitap():
    pass
kitap=Kitap() 
print(kitap)
del kitap  #--> kitap del metoduna sajip degil ama python kafasına gore atıyo
"""

class Kitap():
    def __init__(self, isim,yazar,sayfa,tür):
        print("init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayfa=sayfa
        self.tür=tür


kitap=Kitap("istanbul hatırası","ahmet umit",561,"polisiye")




#init metody 
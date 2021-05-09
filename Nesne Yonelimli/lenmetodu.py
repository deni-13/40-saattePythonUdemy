class Kitap():
    def __init__(self, isim,yazar,sayfa,tür):
        print("init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayfa=sayfa
        self.tür=tür
    def __str__(self):  #string olarak girip 
        return "isim {} yazaR {} SAYFA {}   tür {} ".format(self.isim,self.yazar,self.sayfa,self.tür)

    def __len__(self):
        return self.sayfa


kitap=Kitap("istanbul hatırası","ahmet umit",561,"polisiye")


print(len(kitap))  #len sayfa sayısı 
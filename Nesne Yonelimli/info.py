"""class Araba():    #Burdaki Anlatım Güzel !
    #sınıf ozellikleri
    model="RENAULT"
    renk="yesil"
    silindir=4
#bunlar özellikler

#obje
araba1=Araba()


print(araba1.model)

#farklı degerlerle obje init koycaz

"""
#Init kullanımı
class Araba():
    #sınıf ozellikleri
    def __init__(self,model,renk,silindir):
        print("init cagrıldı")
        self.model=model
        self.renk=renk
        self.silindir=silindir

#---------------------------------------------------

araba1=Araba("BMW i5","mor","4")  #--->her tanımladıgımızda print calısıyor

araba2=Araba("Peugeot","mavi","4")

print(araba2.model)
print(araba)




class Yazılımcı():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim :  {}
        
        Soyisim : {}
        
        Şirket Numarası: {}
        
        Maaş :  {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)
    def maas_yukselt(self,zam_miktarı):
        print("Maaş yükseliyor...")
        
        self.maaş += 250


        

yazılımcı1 =  Yazılımcı("Mustafa Murat","Coşkun",12345,3000,["Python","C","Java"])

yazılımcı1.bilgilerigöster()



yazılımcı1.maas_yukselt(500)  #parametre atamıs bos
yazılımcı1.bilgilerigöster()


yazılımcı1.dil_ekle("Javascript")

yazılımcı1.bilgilerigöster()
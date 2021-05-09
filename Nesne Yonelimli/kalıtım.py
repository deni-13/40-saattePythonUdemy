
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman



class Yönetici(Çalışan): # Çalışan sınıfından miras alıyoruz.
    pass # Pass Deyimi bir bloğu sonradan tanımlamak istediğimizde kullanılan bir deyimdir.



yönetici1 = Yönetici("Mehmet Baltacı",3000,"İnsan Kaynakları") # yönetici objesi


yönetici1.bilgilerigoster() #objeyi metoduyla çagırdık  --> bilgileri goster baska bir klas metodu

yönetici1.departman_degistir("IT")  #Yeni Departman 

yönetici1.bilgilerigoster()


yönetici2=Yönetici("serhat",3500,"Pazarlama")

yönetici2.bilgilerigoster()

#Overriding


class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman


        
class Yönetici(Çalışan): #farklı özellik eklemek için 
    
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı # Yeni eklenen özellik

    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        print("{} {} {} {} " .format(self.isim,self.maaş,self.departman,self.kişi_sayısı) )
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı


yönetici=Yönetici("Oguz",3500,"HR",500)
yönetici.bilgilerigoster()


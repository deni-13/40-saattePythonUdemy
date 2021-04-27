bilgiler = []
Ad = input("Adınız: ")
bilgiler.append(Ad)
Soyadi = input("Soyadınız : ")
bilgiler.append(Soyadi)
Kilo = input("Kilonuz :")
bilgiler.append(Kilo)
Boy = input("Boyunuz : ")
bilgiler.append(Boy)
 
print("Bilgiler kaydediliyor...")
print("Kişi Adı : {}\nKişi Soyadı : {}\nKişi Boyu : {}\nKişiKilosu {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler[3]))
print("Bilgiler Kaydedildi!")
print("""******************************
    Kullanıcı Girişli Program
*****************************""")

#giriş hakkı dongu dısı olmalı 

giris_hakki=3
   
while True :

    sys_username= "deniz"
    sys_password= "adsfdf"
    usernme= input("kullanıcı adı gir")
    parola=input("parola giriniz")

    if(usernme!=sys_username and  parola==sys_password):
        print("kullanıcı adı hatalı")
        giris_hakki-=1

    elif (usernme==sys_username and  parola!=sys_password):
        print("sifre yanlıs")
        giris_hakki-=1

    elif (usernme!=sys_username and  parola!=sys_password):
        print("kullanıcı adı ve sifre yanlıs")
        giris_hakki-=1

    else:
        print("basarılı")
        break

    if(giris_hakki==0):
        print("kilitlendi")
        break

"""
hak=3
 
while True:
    system_kullanici_adi = "ömerahmet"
    system_parola = "142536"
    kullanıcı_adı = input("Kullanıcı Adı Giriniz:")
    parola = input("Parola Giriniz:")
 
    if (system_kullanici_adi == kullanıcı_adı and system_parola != parola):
        print("Parola Hatalı!")
        hak -= 1
 
    elif (system_kullanici_adi != kullanıcı_adı and system_parola == parola):
        print("Kullanıcı Adı Hatalı!")
        hak -= 1
    elif (system_kullanici_adi != kullanıcı_adı and system_parola != parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        hak -= 1
 
    else:
        print("Sisteme Giriş Yapılıyor...")
        break
 
    if (hak == 0):
        print("Daha Sonra Yeniden Deneyiniz...")
        break"""
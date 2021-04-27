
sys_username= "deniz"
sys_password= "adsfdf"
giris_hakki=3
   
while True :

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
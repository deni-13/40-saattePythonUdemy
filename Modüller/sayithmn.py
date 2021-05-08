import random

import time

print("""********************

Sayı tahmin
 1 ve 40 arası tahmin

""")

ras=random.randint(1,40)  #random içinde randint fonksiyonu

tahminhakki=7


while True:

    sayi=int(input("sayi gir"))

    if sayi<ras:
        print("bekle")  
        time.sleep(1)
        print("yukarı")
        tahminhakki-=1


    elif sayi>ras:
    
            print("bekle")  
            time.sleep(1)
            print("aşagı")
            tahminhakki-=1


    else:
        print("tebrikler")
        break
    

    if tahminhakki==0:
        print("bitti sayi--> {}" .format(ras) )
        break 


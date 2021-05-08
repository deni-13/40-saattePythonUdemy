print("""
 
{0}
 
EBOB EKOK bulma programına hoş geldiniz! lütfen seçim yapınız:
 
1: EBOB
2: EKOK
q: Programdan çıkış
 
{0}
 
""".format("*" * 70))
 
def ebob(b,c):
    ortbol = []      # ortak bölenleri bulup listeye atacağız 
    if b > c:        # büyük sayıya göre obeb bulmalıyız
        for i in range(1,b+1):
            if b % i == 0 and c % i == 0:  
                ortbol.append(i) #ikisine birden bölünenleri ekliyoruz
                d = max(ortbol)  #listenin en büyüğünü alıyoruz
    else:  #burada da aynı işlemler, fakat 2. sayının büyük
        for i in range(1,c+1):
            if b % i == 0 and c % i == 0:
                ortbol.append(i)
                d = max(ortbol)
    return d #sonuç olarak en büyük sayıyı geri yolladık
 
def ekok(b,c):
    d = int((b*c) / ebob(b,c)) # evet bu kadar basit :) ebob varsa ekok elimizde
    return d #int yazamamın sebebi yazmazsam 45.0 gibi sonuç vermesi
 
while True:
    a = input("Program seçimi yapınız: ")
    if a == "q":
        print("Güle güle...")
        break
    elif a == "1":
        print("Seçilen işlem: EBOB ")
        b = int(input ("1. sayıyı giriniz: "))
        c = int(input("2. sayıyı giriniz: "))
        if b==0 or c==0:
            print("0' a bölme yapılamaz! tekrar deneyin! ")
            continue
        else:
            d = ebob(b,c)
        print("{} ile {} sayılarının ebob'u {} dir".format(b,c,d))
    elif a == "2":
        print("Seçilen işlem: EKOK ")
        b = int(input("1. sayıyı giriniz: "))
        c = int(input("2. sayıyı giriniz: "))
        if b==0 or c==0:
            print("0' la işlem yapılamaz! tekrar deneyin! ")
            continue
        else:
            d = ekok(b,c)
        print("{} ile {} sayılarının ekok'u {} dir".format(b,c,d))
    else:
        print("Hatalı seçim, tekrar deneyin!")
        continue
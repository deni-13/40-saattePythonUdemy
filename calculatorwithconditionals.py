print("""****************
#elemanlarımız string oldugu icin if/elsede de string koyduk.
hesap makinesi

1.toplama 
2.cıkarma 
3.carpma
4.bolme


***************""")


a=int(input("sayi gir"))
b=int(input("sayi gir"))


islem =input("islem sec")

if islem=="1":
    print(f"islem {a+b}")
elif islem=="2":
     print(f"islem {a-b}")
elif islem=="3":
     print(f"islem {a*b}")

elif islem=="4":
     print(f"islem {a/b} ")

else:
    print("gecersiz!")
    
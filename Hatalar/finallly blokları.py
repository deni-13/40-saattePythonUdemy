#mutlaka çalışması için

try:
    a=int(input("sayi"))
    b=int(input("sayi"))
    print(a/b)

except ValueError:
    print("dogru input gir") #Eger str alırsak
except ZeroDivisionError:
    print("0'a bolunemez")
    
finally:
    print("burası çalıstı")



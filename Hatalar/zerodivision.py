try:
    a=int(input("sayi"))
    b=int(input("sayi"))
    print(a/b)

except ValueError:
    print("dogru input gir") #Eger str alırsak
except ZeroDivisionError:
    print("0'a bolunemez")
    
print("bloklar bitti")



#iki Hatayı aynı bloga yazma


try:
    a=int(input("sayi"))
    b=int(input("sayi"))
    print(a/b)

except( ValueError , ZeroDivisionError): 
    print("Zero Division error veya Value error ") #Eger str alırsak

    
    
print("bloklar bitti")


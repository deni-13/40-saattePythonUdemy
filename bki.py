
a=int(input("Kilonuzu girin"))
b=float(input("Boyunuzu girin metre cinsinden:"))

bki= a / (b**2)

print(f"beden kitle indeksiniz{bki}")

if (bki<18.5):
    print("zayıf")



elif (bki>=18.5 and bki<25):
    print("normal")


elif (bki >= 25 and bki<30):
    print("fazla kilo")



else:
    print("obez")





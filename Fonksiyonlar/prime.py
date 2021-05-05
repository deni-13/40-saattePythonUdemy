#asal sayı

def asalMı(a):
    if a==1:
        return False
    elif a==2:
        return True
    else :
        for i in range(2,a):
            if a%i==0:
                return False

        return True


while True:
    a=input("sayi?")

    if a=="q":
        break
    else: 
        a=int(a)
        if asalMı(a):
            print("asal")
        else:
            print("asal degildir")
        
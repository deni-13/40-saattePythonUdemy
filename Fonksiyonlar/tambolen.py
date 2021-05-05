def tamBolen(sayi):

    tam_bolenler=[]

    for i in range (2,sayi): #bu araarda  bolenleri append ediyor.
        if sayi%i==0:
            tam_bolenler.append(i)

    return tam_bolenler


while True:
        sayi=input("sayi gir")

        if sayi=="q":
            print("sonlandı")
            break
        else:
            sayi=int(sayi)
            print(tamBolen(sayi))
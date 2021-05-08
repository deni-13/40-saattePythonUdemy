def ebob(a,b):
    list1 =[]
    for i in range(1,b+1):
        if (b % i == 0) and (a % i == 0):
            list1.append(i)
    return list1[-1]
 
while True:
    print("Press Q to exit!")
    a = (input("Enter a number:"))
    b = (input("Enter an another number:"))
    if a == "Q" or b == "Q":
        break
    else:
        a = int(a)
        b = int(b)
        print("EBOB:",ebob(a,b))
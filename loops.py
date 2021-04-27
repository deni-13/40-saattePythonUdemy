"""s="python"
for eleman in range(6):
    if eleman % 2 == 0:
        print(s[eleman])"""

"""for i in "python"[::2]:
     print(i,end=" ")"""


    #range fonksiyonu 
#kullanım
#print(*range(0,10))

#geri sayım
#print(*range(20,0,-2))

#---------------------------------------

#list comprenhesion

"""list1=[1,234,56]

list2=list()

for i in list1:
    list2.append(i)
print(list2)"""



#LİST COMPREHENSİON 
lis5=[1,2,3,4,5]
list4= [i for i in lis5]
#sagdan basla burdan okumaya
print(list4)

"""liste1 = [1,2,3,4,5]
liste2 = list(liste1)
 
print(liste2)"""
#aktarım su sekilde de oluyor.

"""
s="java"
list2= [i*3 for i in s]
#s içindeki elemanları 3le list2'ye ekle
print(list2)"""



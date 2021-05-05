"""def selamla():
    print("selam")


selamla()"""



"""icine deger alabilir"""

"""def selamla():
    isim=input("isim?")
   
    print("selam"+isim)
    

selamla()    
    """



""" paramete lerin içi dolu

def selamver(isim):
    print("naber" +isim)

selamver("ali")
"""
"""
def topla(a,b,c):
    print(a+b+c)

topla(6,7,8)"""


#-----Return-----------------------

"""
def topla(a,b,c):
    return (a+b+c)

def ikiylecarp(a):
 return ( 2*a)


toplam=topla(3,4,5)
print(ikiylecarp(toplam))

"""

#----Paramete Türleri ------

def selam(isim):
    print("selam",isim)


selam("murat")

#selam() ---> parametre ver :D

def bilgilerigoster(ad,soyad,numara):
    print("ad:",ad ,"soyad:",soyad, "numara:",numara)

bilgilerigoster("johnny","depp","50")


#Parametre veriyosa parametre gircen



#esnek sayıda degeler
"""
def topla(a,b,c):
    print(a+b+c)

topla(2,3,5,7)""" #calısmıyor



def topla(*a):
    print(a)


topla(2,4,6)


def top(*a):
    toplamm=0
    for i in a:
        toplamm+=i
        print(toplamm)


top(1,2,3)



#--------------------global ve yerel degisken

def fonk():
    a=10 #--->yerel degisken
    print(a)


fonk()
#print(a) calısmaaz NameErro
"""

b=6 #---> global 
def fn():
    print(b)

fn()
"""
#-------------------
#Onemli!!
d=5
def fnk():
    global d #globali 3yaptı yine 3 basıcak
d=3 
print(d)


fnk()
print(d)

 
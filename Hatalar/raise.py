def tersecvir(s):
    if type(s) != str:
        raise ValueError("lutfen str yolla") #hatamızı özellestirdik
    else:
        return s[::-1]


print(tersecvir("naber"))
print(tersecvir(12))


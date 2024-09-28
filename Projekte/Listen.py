

liste = []
liste2 = ["Liste 2 Element", 999]

liste.append("Erstes Element")
liste.append(234)
liste.insert(0,"Insert")

liste.extend(liste2)

print(liste)
print(liste[1])

for element in liste:
    print(type(element) ," ", element)


def test():
    a,b = 1,2
    return a,b

x = test()
print(x)
print(x[0])
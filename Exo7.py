# EXO 1
age = 20
majeur = True
prenom = "Pierre"
come_en_banque = 20135.384
amis = ["Marie", "Julien", "Adrien"]
parents = ("Marc", "Caroline")

affichage_exo = [age, majeur, prenom, come_en_banque, amis, parents]

for x in affichage_exo:
    print(x)

print(" ")
print("__________________")
print(" ")

# EXO 2
print("Exo 2")
site_web = "google"
print(site_web)

print(" ")
print("__________________")
print(" ")

# EXO 3
print("Exo 3")
x = 17
print("La variable est : ", x)

print(" ")
print("__________________")
print(" ")

# EXO 4
print("Exo 4")
a = 3
b = 6
a = b
b = 7
print(6)
print(" ")
print("__________________")
print(" ")

# EXO 5
print("EXO 5")
a = 2
b = 6
c = 3
somme = 0
table = [a, b, c]
for x in table:
    somme += x
    print(x)
print(somme)
print(" ")
print("__________________")
print(" ")


# EXO 6
print("EXO 6")
list1 = range(3)
list2 = range(5)
print(list(list2))

print(" ")
print("__________________")
print(" ")

# EXO 7
print("EXO 7")

def test_type(variable, type):
    if isinstance(variable, type):
        print("C'est ok")
    else:
        print("C'est pas ok")

prenom = "Vincent"
test_type(prenom, str)
prenom = 0
test_type(prenom, int)


print(" ")
print("__________________")
print(" ")

# EXO 8
print("Exo 8")
phrase = "Salut les dev, Salut les gars"
phrase = phrase.replace("Salut", "Bonsoir", 1)
print(phrase)


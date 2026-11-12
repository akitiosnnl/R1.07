nMax = 3
v1 = []
v2 = []
scal = 0


while True:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ?"))
    if n > nMax or n < 1:
        print("valeur incorrecte")
    else:
        break


print("Saisie du premier vecteur :")

for i in range(n):
    a = int(input(f"v1[{i}] = "))
    v1.append(a)


print("Saisie du second vecteur :")

for i in range(n):
    b = int(input(f"v2[{i}] = "))
    v2.append(b)

for i in range(n):
    scal = scal + (v1[i] * v2[i])

print("Le produit scalaire de v1 par v2 vaut", scal)
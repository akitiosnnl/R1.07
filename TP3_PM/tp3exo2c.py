tab1 = []
tab2 = []
tab3 = []

for i in range(0,11):
    valeur = int(input("entrez une valeur :"))
    if valeur < 0 or valeur > 20:
        print("valeur fausse ecrire entre 0 et 20")
        while (valeur < 0 and valeur > 20):
            valeur = int(input("entrez une valeur :"))
            if(valeur > 0 or valeur < 20):
                break
    elif valeur < 10 and valeur >= 0:
        tab1.append(valeur)
    elif valeur >=10 and valeur <15:
        tab2.append(valeur)
    elif valeur >= 15 and valeur <=20:
        tab3.append(valeur)
    else :
        print("erreur inconnue")

print("nombre de valeurs inférieur strictement à 10 :",tab1)
print("nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15  :",tab2)
print("nombre de valeurs supérieur ou égale à 15 :",tab3)
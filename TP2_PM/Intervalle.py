print("l'intervalle est : I = [2,3[ U ]0,1] U [-10,-2]")
x = float(input("Entrez un nombre décimal :"))
if x >= 2 and x < 3:
    print("x appartient a I")
    print("valeur entre 2 (inclus) et 3 (exclus)")
elif x > 0 and x <= 1:
    print("x appartient a I")
    print("valeur entre 0 (exclus) et 1 (inclus)")
elif x >= -10 and x <= -2 :
    print("x appartient a I")
    print("valeur entre -10 (inclus) et -2 (inclus)")
else :
    print("le nombre n'est pas dans l'intervalle")
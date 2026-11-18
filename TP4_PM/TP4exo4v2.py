from collections import Counter

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

occ_max = 0
valeur_max = 0

for i in range(len(L1)) :
    val_traite = L1[i]
    cpt = L1.count(val_traite)
    if cpt > occ_max:
         occ_max = cpt
         valeur_max = val_traite

print(f"Le nombre le plus fréquent dans la liste est le : {valeur_max}({occ_max} x) ")
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

for i in range(len(L1)) :
    val_traite = L1[i]
    cpt = 0
    occ_max = 0
    valeur_max = 0
    for val in L1:
        if val == val_traite:
            cpt += 1
    print(f"Pour {val_traite} on a  {cpt} occurences.")
    if cpt > occ_max:
        occ_max = cpt
        valeur_max = val_traite

print(f"Le nombre le plus fréquent dans la liste est le : {valeur_max}({occ_max} x) ")
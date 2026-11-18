saisie = input("Entrez une date au format jjmmaaaa : ")
date = list(saisie)
jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if len(date) != 8:
    print("Format incorrect ! (8 chiffres attendus sous la forme jjmmaaaa).")
else:
    jour = int(date[0] + date[1])
    mois = int(date[2] + date[3])
    annee = int(date[4] + date[5] + date[6] + date[7])

    if annee == 0:
        print("Date incorrecte : l'année 0000 n'existe pas.")
    elif mois < 1 or mois > 12:
        print("Date incorrecte : le mois doit être compris entre 01 et 12.")
    else:
        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            jours_par_mois[1] = 29
        jours_max = jours_par_mois[mois - 1]

        if jour < 1 or jour > jours_max:
            print("Date incorrecte : ce mois comporte", jours_max, "jours maximum.")
        else:
            print("La date", saisie, "est correcte !")

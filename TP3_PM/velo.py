debut = int(input("Donnez l’heure de début de la location (un entier) :"))
fin =int(input("Donnez l’heure de fin de la location (un entier) :"))
print("Vous avez loué votre vélo pendant ")


heure1 = 0
heure2 = 0

while True :
    if debut > 7 and fin < 17 :
        heure2 = 24-fin-debut
        print(heure2, " heure(s) au tarif horaire de 2.0 euro(s)")
        heure2 = heure2 * 2

    if heure1 > 0 or heure2 > 0 :
        break

    if debut < 7 and fin > 17 :
        heure2 = 24-fin-debut
        print(heure2, " heure(s) au tarif horaire de 1.0 euro(s)")
        heure2 = heure2 * 2

    if heure1 > 0 or heure2 > 0:
        break

    if debut > 17 and fin < 24 :
        heure2 = 40-debut-fin
        print(heure2, " heure(s) au tarif horaire de 1.0 euro(s)")

    if heure1 > 0 or heure2 > 0 :
        break

    if debut > 0 and fin < 7 :
        heure2 = 7-debut-fin
        print(heure2, " heure(s) au tarif horaire de 1.0 euro(s)")

    if heure1 > 0 or heure2 > 0 :
        break

    if heure1 == 0 and heure2 == 0 :
        while True :
            if debut == 0 or debut < 7 :
                heure1 = 7-debut
                print(heure1, " heure(s) au tarif horaire de 1.0 euro(s)")

            if heure1 > 0:
                break

            if debut == 7 or debut <17 :
                heure1 = 17-debut
                print(heure1, " heure(s) au tarif horaire de 2.0 euro(s)")
                heure1 = heure1*2

            if heure1 > 0:
                break

            if debut == 17 or debut > 24 :
                heure1 = 24-debut
                print(heure1, " heure(s) au tarif horaire de 1.0 euro(s)")

            if heure1 > 0:
                break
            break


        while True :
            if fin == 0 or fin < 7 :
                heure2 = 7-fin
                print(heure2, " heure(s) au tarif horaire de 1.0 euro(s)")

            if heure2 > 0:
                break

            if fin == 7 or fin < 17 :
                heure2 = 17-fin
                print(heure2, " heure(s) au tarif horaire de 1.0 euro(s)")

            if heure2 > 0:
                break

            if fin == 17 or fin < 24 :
                heure2 = 24-fin-3
                print(heure2, " heure(s) au tarif horaire de 1.0 euro(s)")

            if heure2 > 0:
                break

            if debut > 7 and fin < 17 :
                heure2 = 24-fin
                print(heure2, " heure(s) au tarif horaire de 2.0 euro(s)")
                heure2 = heure2 * 2

            if heure2 > 0:
                break
            break


heuretot = heure1+heure2
print("Le montant total à payer est de",heuretot,"euro(s).")
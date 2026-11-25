total_notes = 0
total_coeffs = 0
admis = "Oui"

for i in range(1, 6):
    saisie = input("Veuillez entrer la note du module " + str(i) + " et le coefficient correspondant :\n")
    donnees = saisie.split(" ")

    note = float(donnees[0])
    coeff = int(donnees[1])

    total_notes = total_notes + (note * coeff)
    total_coeffs = total_coeffs + coeff

    if note < 8:
        admis = "Non"

moyenne = total_notes / total_coeffs
moyenne = round(moyenne, 2)
print("Moyenne :", moyenne)

if moyenne > 10 and admis == "Oui":
    print("Étudiant admis")
else:
    print("Étudiant non admis")

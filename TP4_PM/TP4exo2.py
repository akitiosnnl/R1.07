# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

for i in range(nombreEtudiants):
    note=float(input("Donnez une note : "))
    while note > 20 or note < 0:
        note = float(input("Donnez une note entre 0 et 20 : "))
    if note <= 20 or note >= 0 :
        notes.append(note)

for i in range(nombreEtudiants):
    moyenne = moyenne + notes[i]

moyenne = moyenne / nombreEtudiants
moyenne = round(moyenne,3)

print("moyenne de classe :", moyenne)

print("Numéro de l’Etudiant | note | écart a la moyenne")
for i in range(nombreEtudiants):
    ecart = moyenne - notes[i]
    print(i,"|",notes[i],"|",ecart)
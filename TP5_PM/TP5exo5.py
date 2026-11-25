salaireh = int(input("Entrer un salaire horaire : "))
h = int(input("Entrer le nombre d'heure travaillées : "))
heuresup = 0
if h <= 160 :
    salairetot = salaireh*h
elif h > 160 and h <= 200 :
    heuresup = h - 160
    salairetot = salaireh*160 + heuresup*1.25
elif h > 200 :
    heuresup = h - 200
    salairetot = salaireh * 160 + 40 * 1.25 + heuresup*1.5

print(f"le salaire finale pour {h}h de travail est de {salairetot}€")
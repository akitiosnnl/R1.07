jour = input("jour du mois :")
jour = int(jour)
heure = input("heure du jour :")
heure = int(heure)
minute = input("minute de heure :")
minute = int(minute)

a = jour*24
a = a+heure
a = a*60+minute

print("le nombre de minute qui se sont écoulés depuis le debut du mois est de " ,a)

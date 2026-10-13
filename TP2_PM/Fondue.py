BASE = 4
fromage = 800
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue:"))
nqfromage = float(fromage * nbConvives / BASE)
nqeau = float(eau * nbConvives / BASE)
nqail = float(ail * nbConvives / BASE)
nqpain = float(pain * nbConvives / BASE)
print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")
print("- ",nqfromage,"gr de fromage")
print("- ",nqeau,"dl d'eau")
print("- ",nqail,"gousse(s) d'ail")
print("- ",nqpain,"gr de pain")
dic={"name":"toto","firstname":"titi","promo":2026,"group":202}
dic2={"name":"tata","firstname":"tutu","promo":2026,"group":102}
binome={"123":dic,"456":dic2}
print("Les clés du dictionnaire sont :")
for key in dic.keys():
    print(f"-{key}")
print("Les valeurs du dictionnaire sont :")
for value in dic.values():
    print(f"-{value}")
print("Les tuplets du dictionnaire sont :")
for item in dic.items():
    print(f"-{item}")

print("Les étudiants formants le binome sont :")
for dic in binome.values():
    print(f"-L'étudiant {dic['name']} {dic['firstname']} du groupe {dic['group']}")
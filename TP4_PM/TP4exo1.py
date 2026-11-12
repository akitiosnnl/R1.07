val=float(input("Vous cherchez la table de multiplication de quel nombre ?"))

x =[0,1,2,3,4,5,6,7,8,9]
y = len(x)

for i in range(0,y):
    z = x[i]
    resultat = z*val
    resultat = round(resultat,2)
    print(val,"*",i,"=",resultat)
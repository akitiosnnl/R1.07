a = int(input("nombre de minute du mois :"))
b = a/60
c = b - int(b)
c = c*60
print("il y a", int(c),"minute")
d = int(b)/24
print("il y a", int(d),"heure")
e = int(a/1440)
print("il y a", int(e),"jour")

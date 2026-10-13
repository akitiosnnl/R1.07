valeur = int(input("Entrez un nombre entier :"))

if valeur == 0:
    print("La valeur est zero (et il est pair)")
elif valeur < 0:
    if valeur%2 == 0:
        print("La valeur est negative et pair")
    else :
        print("La valeur est negative et impair")
elif valeur > 0:
    if valeur%2 == 0:
        print("La valeur est positive et pair")
    else :
        print("La valeur est positive et impair")
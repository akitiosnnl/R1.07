b100 = 0
b50 = 0
b10 = 0
b2 = 0
b1 = 0

somme = int(input("Entrez la somme d'argent en euros : "))
reste = somme

billets_100 = reste // 100
reste = reste % 100

billets_50 = reste // 50
reste = reste % 50

billets_10 = reste // 10
reste = reste % 10

pieces_2 = reste // 2
pieces_1 = reste % 2

print(f"{somme} euros, c’est donc {billets_100} billets de 100, {billets_50} de 50, {billets_10} de 10, {pieces_2} pièces de 2 et {pieces_1} pièce 1.")


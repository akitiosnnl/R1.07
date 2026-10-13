import random
valeur = random.randint(1,100)
tour =0
while True :
    a = int(input("devine le nombre :"))
    if a == valeur :
        tour = tour + 1
        print("Trouve ! La valeur etait bien",valeur)
        print("tu a trouver au bout du", tour,"eme tour")
        break
    elif a > valeur :
        print("plus petit")
    elif a < valeur :
        print("plus grand")
    tour = tour + 1
    print("tour :",tour)
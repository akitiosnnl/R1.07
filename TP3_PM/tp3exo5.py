fact = 0
n = int(input("choisir la factorielle :"))
print("choisir la methode pour déterminer la factorielle")
print("1.For")
print("2.While ")
choix = int(input("choisir une methode :"))
if choix ==1 :
    for i in range(0,n+1) :
        fact = fact*i
        print(fact)
x = int(input("entrez une valeur :"))
a = 0
for i in range(0,x+1):
    a = a + i
    if a == x:
        print(i)
        break
    elif a > x:
        int(i)
        print(i-1)
        break

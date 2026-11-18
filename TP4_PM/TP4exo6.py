tab = [5, 2, 4, 8, 1, 3]

print("methode for")
for i in range(len(tab)):
    min = i
    for j in range(i + 1, len(tab)):
        if tab[j] < tab[min]:
            min = j
    print(tab)
    tab[i], tab[min] = tab[min], tab[i]

print("methode print(sorted(tab))")
print(sorted(tab))

print("methode tab.sort()")
tab.sort()
print(tab)
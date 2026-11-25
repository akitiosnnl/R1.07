chaine = input("Entrez un mot ou une phrase : ")

chaine2 = ""
for c in chaine2.lower():
    if c.isalpha():
        chaine2 += c

est_palindrome = True
longueur = len(chaine2)

for i in range(longueur // 2):
    if chaine2[i] != chaine2[longueur - 1 - i]:
        est_palindrome = False
        break

if est_palindrome:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")

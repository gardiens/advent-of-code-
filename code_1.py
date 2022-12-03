dict = {}
i = 0
"""with open('test.txt') as f:
    lignes = f.readlines()
    print(lignes)
    for ligne in lignes.splitlines():
 
        ligne = ligne.strip() # on retire d'éventuels espaces avant et après
        #ligne=ligne.rstrip('\n')
 
     if ligne=="":
        i+=1
 
     nb = ligne.split()[-1] # on prend la dernière chaine après le dernier espace
 
     if '.' in nb or 'E' in nb:
        nb = float(nb) # c'est un nb flotant
     else:
         nb = int(nb) # c'est un entier
 
     print(nb) # affichage du nombre
   
     pass
"""
# récupère tous les entiers présent dans le .txt
i = 0
dict = {0: 0}
with open('test.txt') as f:
    lignes = f.readlines()
    for ligne in lignes:
        l = ligne.split()
        if len(l) == 0:
            i += 1
            dict[i] = 0
        else:
            dict[i] = dict[i]+int(l[0])

print(dict)


L = []
n = 3
for _ in range(3):
    max = 0
    key = -1
    for keys in dict:
        if dict[keys] > max and keys not in L:
            max = dict[keys]
            key = keys
    L.append(key)

print("liste des trucs interessant", L)
print(" les 3 cherchés", sum(dict[k] for k in L))

#print("le maximum vaut,", max(dict.values()))

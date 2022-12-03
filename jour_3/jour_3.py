import string as string


def recup_element_from_set(set):
    for element in set:
        break
    return element


def priority_level(s):
    if s.isupper():
        return string.ascii_uppercase.index(s)+27

    else:
        return string.ascii_lowercase.index(s)+1


def parse(jour, inputname):
    with open('./jour_3/input.txt') as f:
        lignes = f.readlines()
        score = 0
        monteur = 0
        L = []
        for ligne in lignes:
            l = ligne.split()
            # print(l)
            t = l[0]  # le mot

            n = len(t)
            # print(n)
            nu = int(n/2)
            # print(nu)

            mot1, mot2 = t[0:nu], t[nu:n]
            character = recup_element_from_set(
                set(mot1).intersection(set(mot2)))
            score += priority_level(character)
        return score

        # print(mot1, mot2)


def parse_2(jour, inputname):
    with open('./jour_3/input.txt') as f:
        lignes = f.readlines()
        score = 0
        monteur = 0
        L = []
        for ligne in lignes:
            l = ligne.split()
            # print(l)
            t = l[0]  # le mot
            print(monteur)
            if monteur == 0:
                L = [t]
                monteur += 1
            else:
                monteur += 1
                L.append(t)

            if monteur == 3:
                mot1, mot2, mot3 = L[0], L[1], L[2]
                print(mot1, mot3)
                character = recup_element_from_set(
                    set(mot1).intersection(set(mot2)).intersection(set(mot3)))
                monteur = 0

                score += priority_level(character)
        return score

        # print(mot1, mot2)


inputname = 'input.txt'
jour = './jour3/'
a = parse_2(jour, inputname)
print('AAA', a)

# print(priority_level('a'))

# print(priority_level('A'))

print(priority_level('A'))



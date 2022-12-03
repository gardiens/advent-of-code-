i = 0
dict = {0: 0}
score = 0
'X:Rock'

'''with open('./jour_2/texte.txt') as f:
    lignes = f.readlines()
    for ligne in lignes:
        l = ligne.split()
        #print(l[0], l[1])
        if l[0] == 'A':

            if l[1] == 'X':
                nb = 1
                score += nb+3

            if l[1] == 'Y':
                nb = 2
                score += nb+6

            if l[1] == 'Z':
                nb = 3
                score += nb+0

        if l[0] == 'B':

            if l[1] == 'X':
                nb = 1
                score += nb+0

            if l[1] == 'Y':
                nb = 2
                score += nb+3

            if l[1] == 'Z':
                nb = 3
                score += nb+6

        if l[0] == 'C':

            if l[1] == 'X':
                nb = 1
                score += nb+6

            if l[1] == 'Y':
                nb = 2
                score += nb+0

            if l[1] == 'Z':
                nb = 3
                score += nb+3


print('score:', score)

'''
print(dict)

# Cas 2
# A Rock B Paper C scissors
# X  Rock Y Paper Z scissors
# Y: draw X loze W win
score_choix = {'X': 1, 'Y': 2, 'Z': 3}

# t sera déterminé par nous même
with open('./jour_2/texte.txt') as f:
    lignes = f.readlines()
    for ligne in lignes:
        l = ligne.split()
        #print(l[0], l[1])
        if l[0] == 'A':  # Rock
            if l[1] == 'X':
                # lose
                t = 'Z'
                u = 0
            if l[1] == 'Y':  # Draw
                t = 'X'
                u = 3

            if l[1] == 'Z':  # win
                t = 'Y'
                u = 6

            if t == 'X':
                # lose

                nb = 1
                score += nb+u

            if t == 'Y':
                nb = 2
                score += nb+u

            if t == 'Z':
                nb = 3
                score += nb+u

        if l[0] == 'B':  # Paper
            if l[1] == 'X':  # lose
                # lose
                t = 'X'
                u = 0
            if l[1] == 'Y':
                t = 'Y'
                u = 3

            if l[1] == 'Z':
                t = 'Z'
                u = 6

            if t == 'X':
                nb = 1
                score += nb+u

            if t == 'Y':
                nb = 2
                score += nb+u

            if t == 'Z':
                nb = 3
                score += nb+u

        if l[0] == 'C':  # scissors
            if l[1] == 'X':
                # lose
                t = 'Y'
                u = 0

            if l[1] == 'Y':
                t = 'Z'
                u = 3

            if l[1] == 'Z':
                t = 'X'
                u = 6
            if t == 'X':
                nb = 1
                score += nb+u

            if t == 'Y':
                nb = 2
                score += nb+u

            if t == 'Z':
                nb = 3
                score += nb+u


print("exo 2, score:", score)

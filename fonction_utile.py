def parse(inputname):
    with open(inputname) as f:
        lignes = f.readlines()
        for ligne in lignes:
            l = ligne.split()
            # l=[ le truc àl'intérieur]


inputname = 'texte.txt'

text_file = open('./jour_n/input.txt')
# renvoie une liste avec tous les caractères !!!!
rucksacks = text_file.read().strip().split('\n')

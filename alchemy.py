# A simple infintely expandable alchemy sim :)
import csv
from time import sleep

unlocked = ['fire', 'water', 'air', 'earth']
combine = {}

def import_combos():
    with open('combos.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            combo = tuple(sorted((line[0], line[1])))
            combine[combo] = line[2]

def find_match(a, b):
    if a in unlocked and b in unlocked:
        try:
            out = combine[tuple(sorted((a, b)))]
            print('\n\nCombination Success!!!')
            if out not in unlocked:
                print('New element unlocked:', out+'\n\n')
                unlocked.append(out)
            else:
                print('Element already unlocked:', out+'\n\n')
            
        except KeyError:
            print('\n\nCombination Failed!\n')
    else:
        print('\nInvalid element used\n')

import_combos()

while True:
    print('-'*20)
    print('Available Elements ({}/{}): '.format(len(unlocked), len(combine)+4))
    print(*unlocked, sep=', ')
    a = input('\nInput One: ').lower()
    b = input('Input Two: ').lower()

    print('\nAttempting to combine', end='')
    for i in range(5): sleep(0.5); print('.', end='')

    find_match(a, b)


#Coin flip streaks

import random

numberOfStreaks = 0 

for experimentNumber in range(10000):

    #Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(100):
        if random.randint(0, 1):
            flips.append('H')
            print('HEADS') #For fun!
        else:
            flips.append('T')
            print('TAILS')

    #Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(100-6):
        if flips[i] == flips[i+1] == flips[i+2] == flips[i+3] == flips[i+4] == flips[i+5]:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))



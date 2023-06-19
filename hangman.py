import random
from functions import *
from components import *

# Pre-requisite
correct = []
wrong = []
lst = opmore # list choice to pick from
sw = random.choice(lst).lower()
secret_word = sw[:]
sw_check = set(list(secret_word))
sw_check.discard(' ')
# print(list(secret_word)) #ANS
# Game Start
chances = 5
game = True

while game:
    print('++++++++++++++++++++++++++')
    print('       H-A-N-G-M-A-N      ')
    print('++++++++++++++++++++++++++')
    chance_left = chances - len(wrong)
    print(f'Chances left: {chance_left}')
    print(f'Wrong characters: {wrong}')
    print(hang_block[chance_left])
    if set(correct) == sw_check:
        # print(correct)
        # print(sw_check)
        print(reset(secret_word, correct))
        print('XXXXXXXXXXXX........Congratulations........XXXXXXXXXXX')
        break
    elif chance_left <= 0:
        game = False
    else:
        print(reset(secret_word, correct))
        guess = input('Input your guess...')
        check(sw, correct, wrong, guess)
    print('\n')




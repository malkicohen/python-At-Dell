
import random
rand_number = random.randrange(1, 10)
while True:
    guess = input('Please guess a number!')
    if int(guess) == rand_number or guess == 'q':
        break
    elif int(guess) > rand_number:
        print('Bigger than the random')
    else:
        print('Smaller than the random')



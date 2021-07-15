'''Program to roll a dice '''
import random

choice = input('Want to roll a dice ? (Y/N)')
while (choice == 'Y'):
    if choice == 'Y':
        print(' The number is : ' + str(random.randint(1,6)))
    else:
        exit = input('Not a valid choice , want to exit ? (Y/N)')
        if exit == 'N':
            print('Thank You for playing!')


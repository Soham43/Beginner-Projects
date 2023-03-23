name = input('Type your Name: ')
print('Welcome', name, 'to your first adventure')

answer = input('You are on a dirt road , it has come to an end and you can go \"Left\" or \"Right\". Which way would you like to go?: ').lower()

if answer == 'left':
    answer = input('You have reached the river, you can walk around or swim accross. Type \"Walk\" to walk around or \"Swim\" to swim across: ').lower()

    if answer == 'swim':
        print('You Swam across and were eaten by an alligator')
    elif answer == 'walk':
        print('You walked for many Kilometeres and ran out of water and died')
    else:
        print('Invalid Option, You Lose!')

elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly. Do you want to cross it or go back?(cross/back): ').lower()
    
    if answer == 'back':
        print('You were not brave enough, You lose')
    elif answer == 'cross':
        answer = input('You cross the bridge and meet a stranger, Do you talk to them?(yes/no): ').lower()

        if answer == 'yes':
            print('The stranger gives you a gold coin and you win')
        elif answer == 'no':
            print('you ignored the stranger and missed an important oppertunity and you lose')
        else:
             print('Invalid Option, You Lose!')       
    else:
        print('Invalid Option, You Lose!')
else:
    print('Invalid option. you lose!')

print('Thank you for trying', name)
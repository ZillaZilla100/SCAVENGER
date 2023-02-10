from pyfiglet import figlet_format
import random
import sys
import time


def typewriter(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)


buildings = ['Franklin D. High School', 'World Fitness', '7twelve', 'Church', 'Uncle Sam\'s Club', '99 Cents Store', 'Bed, Bath, and Whatever', 'Home Supply Depot',
             '145 9th St. Residence', '489 12th St. Residence', '390 Gleen Blvd. Residence', 'Waffle House', 'Uhop', 'Jerry\'s Diner', 'Lookers Sports Bar', 'Chip \'n\' Tales']


foods = ['Baked Beans', 'Tuna', 'SPAM', 'Potted Meat', 'Canned Vegatables', 'M.R.E.',
         'Stale Pringles', 'Chef Boy-R-Dee', 'Bottled Water', 'Twinkies', 'Ding-Dongs', 'Rotel']


stash = []

day_number = 0

hunger = 5

raider_encounters = 0
buildings_looted = 0 
food_ate = 0

def end_screen():
    print(figlet_format('        W A S T E D', font= 'doom'))
    typewriter('\nWhat was left of this world will miss you...\nHere are the stats for your latest session\n')

    print('DAYS SURVIVED:', day_number)
    print('BUILDINGS LOOTED:', buildings_looted)
    print('FOOD ITEMS CONSUMED:', food_ate)
    print('TIMES YOU ENCOUNTERED RAIDERS:', raider_encounters)

    x = input('Press Enter to Exit\n')
    if x == '':
        quit()

# end_screen()

#function used to determine how many and which food items are looted.
def food():
    chance = random.randint(0, 100)
    # print(chance)
    if chance <= 50:
        x = random.choice(foods)
        typewriter('You were able to SCAVENGE one item...')
        print('\n\'' + x + '\'')
        typewriter('You make your way back home without meeting raiders...\n')
        print(x, 'Has been added to your stash')
        stash.append(x)
        time.sleep(1)
        # print(stash)

    if chance > 50 and chance <= 80:
        x = random.sample(foods, 2)
        typewriter('You managed to SCAVENGE 2 items...')
        print('\n\'' + x[0] + '\'\n''\'' + x[1] + '\'')
        typewriter('You sneak back home without detection...\n')
        print(x[0], 'and', x[1], 'have been added to your stash')
        stash.append(x[0])
        stash.append(x[1])
        time.sleep(1)
        # print(stash)

    if chance > 80:
        typewriter('You were NOT able to SCAVENGE anything...')
        typewriter('You return home empty handed...\n')
        time.sleep(1)
    home_menu()

# food()

#functin used to deal with raiders at night and the day counter. Chance of raiders raiding increases with the days.
def sleepy_time():
    global day_number
    day_number += 1
    global hunger
    hunger -= 1
    global raider_encounters

    message = ['\nWith the sound of raiders in the distance, you slowly fall asleep...', '\nTossing and turning thru the night, you manage to get some rest...', '\nYou dream of days past without the apocalypse at hand...',
               '\nFor what its worth you get some sleep...', '\nThe sounds of critters in the wall act as white noise while you sleep...', '\nThe cold bedding carries you to a deep sleep...', '\nWithout knowing what tomorrow brings, you doze off peacefully...']

    message_raider = ['\nRaiders came thru the night emptying out your STASH...', '\nYou hear a loud bang... You get up to see raiders leaving with your STASH...',
                      '\nYou wake to a raider standing above you with his friends stealing your STASH...', '\nYou wake to raiders talking about your stash.. You lay quiet while they steal your STASH']

    if hunger < 0:
        typewriter('\nYou try to sleep but your stomach wont let you. You die from starvation in your cold bedding....')
        end_screen()

    if day_number <= 3:
        for i in random.choice(message):
            typewriter(i)
        print('\nHunger has gone down by 1')

    if day_number > 3 and day_number <= 5:
        x = random.randint(0, 100)
        if x <= 90:
            for i in random.choice(message):
                typewriter(i)
            print('\nHunger has gone down by 1\n')

        if x > 90:
            for i in random.choice(message_raider):
                typewriter(i)
            print('\nYour STASH has been emptied')
            print('Hunger has gone down by 1')
            raider_encounters += 1

    if day_number > 5 and day_number <= 10:
        x = random.randint(0, 100)
        if x <= 75:
            for i in random.choice(message):
                typewriter(i)
            print('\nHunger has gone down by 1')

        if x > 75:
            for i in random.choice(message_raider):
                typewriter(i)
            print('\nYour STASH has been emptied')
            print('Hunger has gone down by 1')
            raider_encounters += 1

    if day_number > 10:
        x = random.randint(0, 100)
        if x <= 50:
            for i in random.choice(message):
                typewriter(i)
            print('\nHunger has gone down by 1')

        if x > 50:
            for i in random.choice(message_raider):
                typewriter(i)
            print('\nYour STASH has been emptied')
            print('Hunger has gone down by 1')
            raider_encounters += 1

    # print(day_number)
    #used to show new day has begun with cool ascii text
    time.sleep(1)
    print(figlet_format('                     D A Y  ' + str(day_number+1), font='doom'))

    time.sleep(0.5)
    home_menu()


# sleepy_time()

# stash = ['chips','bag','crack']

#function used for dealing with inventory and adding hunger back to hunger lvl
def pantry():
    global hunger
    global food_ate
    print(figlet_format('            S T A S H', font='small'))
    for count, x in enumerate(stash, 1):
        print(count, ')', x)

    if len(stash) == 0:
        typewriter('You have no items to consume...\n')
        time.sleep(1)
        home_menu()

    choice = int(input(
        'Which item to you wish to consume? 1,2,3,etc. Or enter \'100\' to return to HOME BASE MENU \n'))

    if choice < 100:
        typewriter('You dig into the ')
        print('\'' + stash[choice-1] + '\'')
        stash.pop(choice-1)
        print('Hunger has increased by 2')
        time.sleep(1)
        hunger += 2
        food_ate += 1
        home_menu()
    # print(stash)

    if choice == 100:
        typewriter('Back to Home Base Menu\n')
        time.sleep(1)
        home_menu()

# pantry()

#function used for raider encounter on the way to get food. Doesnt increase with days
def raider():
    global buildings_looted
    global raider_encounters
    chance = random.randint(0, 100)
    # print(chance)
    if chance < 75:
        message1 = ['You sneak safely thru the raiders...\n',
                    'You barely miss 2 raiders on the way there...\n', 'You made it with no hassle from the raiders...\n']

        for i in random.choice(message1):
            typewriter(i)
        buildings_looted += 1
        food()

    else:
        message2 = ['Raiders have captured you, but decided to let you go because you had nothing on you...\nYou gain no food and return home...\n',
                    'Raiders corner you, but you narrowly escape... You return home with no food today...\n']

        for i in random.choice(message2):
            typewriter(i)
        raider_encounters += 1
        time.sleep(2)
        home_menu()

# raider()

#function used for displaying loot location options and decrease hunger when ran
def rand_buildings():
    global hunger 
    hunger -= 1
    if hunger < 0:
        typewriter('\nYou start to head out with your stomach rumbling, you don\'t make it far before you collapse from starvation...')
        end_screen()

    a = random.sample(buildings, 3)
    # print(a)
    print(figlet_format('L o o t  L o c a t i o n s', font='small'))
    print('1) ' + a[0])
    print('2) ' + a[1])
    print('3) ' + a[2])
    print('4) More buildings.....')

    typewriter('\nChoose your looting location:')
    x = input('')
    text = ['You leave at first light towards ',
            'You break at dawn for ', 'You sneak in the morning fog to ']


    if x == '1':
        typewriter(random.choice(text) + a[0] + '\n')
        raider()

    if x == '2':
        typewriter(random.choice(text) + a[1] + '\n')
        raider()

    if x == '3':
        typewriter(random.choice(text) + a[2] + '\n')
        raider()

    if x == '4':
        rand_buildings()

    else:
        home_menu()

# rand_buildings()

#function for home menu looks and choice
def home_menu():
    print(figlet_format('  H O M E    B A S E '))
    print('______________________________________________________________________')
    print('|                                  ||                                |')
    print('|      \u03321   SCAVENGE (-1 Hunger)    ||         \u03323   STASH/EAT          |')
    print('|__________________________________||________________________________|')
    print('|                                  ||                                |')
    print('|       \u03322   SLEEP (-1 Hunger)      ||         \u03324   HELP/STATS         |')
    print('|__________________________________||________________________________|')
    print('                  |                                  |                ')
    print('                  |          \u03325   GIVE UP             |                ')
    print('                  |__________________________________|                ')
    print('      You have made it to day',
          day_number, 'so far, Current hunger level is', hunger,'                 \n\n')

    choice = input('Choose an option: ')
    if choice == '1':
        rand_buildings()
    elif choice == '2':
        typewriter('You get ready to lay down...')
        sleepy_time()
    elif choice == '3':
        pantry()
    elif choice == '4':
        
        print('\nSleep and Scavenge remove 1 hunger point. \nEating will restore 2 per item. \nIf hunger drops below 0, you die from starvation. \n')
        print('DAYS SURVIVED:', day_number)
        print('BUILDINGS LOOTED:', buildings_looted)
        print('FOOD ITEMS CONSUMED:', food_ate)
        print('TIMES YOU ENCOUNTERED RAIDERS:', raider_encounters)
        x = input('Press ENTER to return to menu\n')
        if x == '':
            home_menu()
    elif choice == '5':
        typewriter('\nYou have decided to give up and starve to death...')
        end_screen()
    else:
        home_menu()

#home_menu()

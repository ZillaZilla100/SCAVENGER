from pyfiglet import figlet_format
import random
import sys
import time








def add_counter(n):
    return n + 1

def sub_counter(n):
    return n - 1

def typewriter(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)


def day_art(day_number):
    #used to show new day has begun with cool ascii text
    time.sleep(1)
    print(figlet_format('                     D A Y  ' + str(day_number), font='doom'))
    time.sleep(0.5)
    return day_number

def clear_stash(cs):
    if cs == 1:
        stash.clear()
        return stash


def sleepy_time(hunger, raider_encounters, day_number):
    #function used for adding hunger, day, and raid possibilty at sleep option
    
    message = ['\nWith the sound of raiders in the distance, you slowly fall asleep...', '\nTossing and turning thru the night, you manage to get some rest...', '\nYou dream of days past without the apocalypse at hand...',
               '\nFor what its worth you get some sleep...', '\nThe sounds of critters in the wall act as white noise while you sleep...', '\nThe cold bedding carries you to a deep sleep...', '\nWithout knowing what tomorrow brings, you doze off peacefully...']

    message_raider = ['\nRaiders came thru the night emptying out your STASH...', '\nYou hear a loud bang... You get up to see raiders leaving with your STASH...',
                      '\nYou wake to a raider standing above you with his friends stealing your STASH...', '\nYou wake to raiders talking about your stash.. You lay quiet while they steal your STASH']

    if hunger == 0:
        typewriter('\nYou try to sleep but your stomach wont let you. You die from starvation in your cold bedding....')
        
        end_screen(hunger, day_number, raider_encounters, food_ate, buildings_looted)

    if day_number <= 3:
        for i in random.choice(message):
            typewriter(i)
        print('\nHunger has gone down by 1')
        hunger = sub_counter(hunger)
        day_number = add_counter(day_number)
        day_number = day_art(day_number)
        return hunger, raider_encounters, day_number

    if day_number > 3 and day_number <= 5:
        x = random.randint(0, 100)
        if x <= 85:

            for i in random.choice(message):
                typewriter(i)
            print('\nHunger has gone down by 1\n')
            hunger = sub_counter(hunger)
            day_number = add_counter(day_number)
            day_number = day_art(day_number)
            return hunger, raider_encounters, day_number

        if x > 85:

            for i in random.choice(message_raider):
                typewriter(i)
            print('\nYour STASH has been emptied')
            print('Hunger has gone down by 1')
            hunger = sub_counter(hunger)
            raider_encounters = add_counter(raider_encounters)
            day_number = add_counter(day_number)
            day_number = day_art(day_number)
            clear_stash(1)
            return hunger, raider_encounters, day_number
            

    if day_number > 5 and day_number <= 10:
        x = random.randint(0, 100)
        if x <= 75:
            for i in random.choice(message):
                typewriter(i)
            print('\nHunger has gone down by 1')
            hunger = sub_counter(hunger)
            day_number = add_counter(day_number)
            day_number = day_art(day_number)
            return hunger, raider_encounters, day_number
            

        if x > 75:
            for i in random.choice(message_raider):
                typewriter(i)
            print('\nYour STASH has been emptied')
            print('Hunger has gone down by 1')
            hunger = sub_counter(hunger)
            raider_encounters = add_counter(raider_encounters)
            day_number = add_counter(day_number)
            day_number = day_art(day_number)
            clear_stash(1)
            return hunger, raider_encounters, day_number
            

    if day_number > 10:
        x = random.randint(0, 100)
        if x <= 50:
            for i in random.choice(message):
                typewriter(i)
            print('\nHunger has gone down by 1')
            hunger = sub_counter(hunger)
            day_number = add_counter(day_number)
            day_number = day_art(day_number)
            return hunger, raider_encounters, day_number

        if x > 50:
            for i in random.choice(message_raider):
                typewriter(i)
            print('\nYour STASH has been emptied')
            print('Hunger has gone down by 1')
            hunger = sub_counter(hunger)
            raider_encounters = add_counter(raider_encounters)
            day_number = add_counter(day_number)
            day_number = day_art(day_number)
            clear_stash(1)
            return hunger, raider_encounters, day_number
    

'''
print(hunger)
print(raider_encounters)
print(day_number)

hunger = 5
day_number = 10
raider_encounters = 0
food_ate = 0
buildings_looted = 0

hunger, raider_encounters, day_number = sleepy_time(hunger, raider_encounters, day_number)

print(stash)

print(hunger)
print(raider_encounters)
print(day_number)
'''

def pantry(hunger, food_ate):
# function for showing stash and consuming food
    
    print(figlet_format('            S T A S H', font='small'))
    for count, x in enumerate(stash, 1):
        print(count, ')', x)

    if len(stash) == 0:
        typewriter('You have no items to consume...\n')
        time.sleep(1)
        return hunger, food_ate

    choice = int(input(
        'Which item to you wish to consume? 1,2,3,etc. Or enter \'100\' to return to HOME BASE MENU \n'))

    if choice < 100:
        typewriter('You dig into the ')
        print('\'' + stash[choice-1] + '\'')
        stash.pop(choice-1)
        print('Hunger has increased by 2')
        time.sleep(1)
        hunger = hunger + 2
        food_ate = add_counter(food_ate)
        return hunger, food_ate
    # print(stash)

    if choice == 100:
        typewriter('Back to Home Base Menu\n')
        time.sleep(1)
        return hunger, food_ate

'''
print(hunger)
print(food_ate)

hunger, food_ate = pantry(hunger, food_ate)

print(hunger)
print(food_ate)
'''


def food():
# function to determine what food is looted from rand_buildings
    chance = random.randint(0, 100)
    # print(chance)
    if chance <= 60:
        x = random.choice(foods)
        typewriter('You were able to SCAVENGE one item...')
        print('\n\'' + x + '\'')
        typewriter('You make your way back home without meeting raiders...\n')
        print(x, 'Has been added to your stash')
        stash.append(x)
        time.sleep(1)
        # print(stash)

    if chance > 60 and chance <= 90:
        x = random.sample(foods, 2)
        typewriter('You managed to SCAVENGE 2 items...')
        print('\n\'' + x[0] + '\'\n''\'' + x[1] + '\'')
        typewriter('You sneak back home without detection...\n')
        print(x[0], 'and', x[1], 'have been added to your stash')
        stash.append(x[0])
        stash.append(x[1])
        time.sleep(1)
        # print(stash)

    if chance > 90:
        typewriter('You were NOT able to SCAVENGE anything...')
        typewriter('You return home empty handed...\n')
        time.sleep(1)
    return



def rand_buildings(hunger, raider_encounters, buildings_looted):
#function used to show options for looting, possible raider encounter

    while True:
        a = random.sample(buildings, 3)
        # print(a)
        print(figlet_format('L o o t  L o c a t i o n s', font='small'))
        print('1) ' + a[0])
        print('2) ' + a[1])
        print('3) ' + a[2])
        print('4) Search for more locations...')

        typewriter('\nChoose your looting location:')
        x = int(input(''))
        text = ['You leave at first light towards ',
                'You break at dawn for ', 'You sneak in the morning fog to ']

        chance_raiders = random.randint(0, 100)

        if chance_raiders > 80:
            message2 = ['Raiders have captured you, but decided to let you go because you had nothing on you...\nYou gain no food and return home...\n',
                    'Raiders corner you, but you narrowly escape... You return home with no food today...\n']

            for i in random.choice(message2):
                typewriter(i)

            time.sleep(2)

            raider_encounters = add_counter(raider_encounters)
            hunger = sub_counter(hunger)
            return(hunger, raider_encounters, buildings_looted)

        if x == 1:
            typewriter(random.choice(text) + a[0] + '\n')
            hunger = sub_counter(hunger)
            buildings_looted = add_counter(buildings_looted)
            food()
            return hunger, raider_encounters, buildings_looted

        if x == 2:
            typewriter(random.choice(text) + a[1] + '\n')
            hunger = sub_counter(hunger)
            buildings_looted = add_counter(buildings_looted)
            food()
            return hunger, raider_encounters, buildings_looted
            
        if x == 3:
            typewriter(random.choice(text) + a[2] + '\n')
            hunger = sub_counter(hunger)
            buildings_looted = add_counter(buildings_looted)
            food()
            return hunger, raider_encounters, buildings_looted
            
        if x == 4:
            continue


'''
print(hunger)
print(raider_encounters)
print(buildings_looted)

hunger, raider_encounters, buildings_looted = rand_buildings(hunger, raider_encounters, buildings_looted)

print(hunger)
print(raider_encounters)
print(buildings_looted)
'''

def end_screen(hunger, day_number, raider_encounters, food_ate, buildings_looted):
    print(figlet_format('        W A S T E D', font= 'doom'))
    typewriter('\nWhat was left of this world will miss you...\nHere are the stats for your latest session\n')

    print('DAYS SURVIVED:', day_number)
    print('BUILDINGS LOOTED:', buildings_looted)
    print('FOOD ITEMS CONSUMED:', food_ate)
    print('TIMES YOU ENCOUNTERED RAIDERS:', raider_encounters)

    x = input('Press Enter to Exit\n')
    if x == '':
        quit()


def start():
    print(figlet_format('    S C A V E N G E R', font='doom'))
    print(figlet_format('A TEXT GAME', font='chunky'))

    typewriter('Just another day in the wasteland...\nYou must SCAVENGE for food or DIE!!!\nYour stockpiles are low and raiders have entered your town.\nSave what you can and eat when you have to.\nSURVIVE AS LONG AS POSSIBLE!!!\n')



def home_menu(hunger, day_number, raider_encounters, food_ate, buildings_looted):
#function for home menu looks and choice

    print(figlet_format('  H O M E    B A S E '))
    print('______________________________________________________________________')
    print('|                                  ||                                |')
    print('|      1   SCAVENGE (-1 Hunger)    ||         3   STASH/EAT          |')
    print('|__________________________________||________________________________|')
    print('|                                  ||                                |')
    print('|       2   SLEEP (-1 Hunger)      ||         4   HELP/STATS         |')
    print('|__________________________________||________________________________|')
    print('                  |                                  |                ')
    print('                  |          5   GIVE UP             |                ')
    print('                  |__________________________________|                ')
    print('      You have made it to day',
          day_number, 'so far, Current hunger level is', hunger,'                 \n\n')

    
    if hunger == 0:
        typewriter('\nIt\'s a cold world out there SCAVENGING for food amongst the raiders. This life just wasn\'t yours to live. You die from starvation....\n')
        
        end_screen(hunger, day_number, raider_encounters, food_ate, buildings_looted)
    
    choice = input('Choose an option: ')

    if choice == '1':
        
        hunger, raider_encounters, buildings_looted = rand_buildings(hunger, raider_encounters, buildings_looted)
        return hunger, day_number, raider_encounters, food_ate, buildings_looted

    elif choice == '2':
        
        typewriter('You get ready to lay down...')
        #sleepy_time(hunger, raider_encounters, day_number)
        hunger, raider_encounters, day_number = sleepy_time(hunger, raider_encounters, day_number)
        return hunger, day_number, raider_encounters, food_ate, buildings_looted

    elif choice == '3':

        hunger, food_ate = pantry(hunger, food_ate)
        return hunger, day_number, raider_encounters, food_ate, buildings_looted

    elif choice == '4':
        
        print('\nSleep and Scavenge remove 1 hunger point. \nEating will restore 2 per item. \nIf hunger drops below 0, you die from starvation. \n')
        print('DAYS SURVIVED:', day_number)
        print('BUILDINGS LOOTED:', buildings_looted)
        print('FOOD ITEMS CONSUMED:', food_ate)
        print('TIMES YOU ENCOUNTERED RAIDERS:', raider_encounters)
        x = input('Press ENTER to return to menu\n')
        if x == '':
            return hunger, day_number, raider_encounters, food_ate, buildings_looted


    elif choice == '5':

        typewriter('\nYou have decided to give up and starve to death...\n')
        end_screen(hunger, day_number, raider_encounters, food_ate, buildings_looted)
    
    else:
        return hunger, day_number, raider_encounters, food_ate, buildings_looted



#starting variables for the game

buildings = ['Franklin D. High School', 'World Fitness', '7twelve', 'Church', 'Uncle Sam\'s Club', '99 Cents Store', 'Bed, Bath, and Whatever', 'Home Supply Depot',
             '145 9th St. Residence', '489 12th St. Residence', '390 Gleen Blvd. Residence', 'Waffle House', 'Uhop', 'Jerry\'s Diner', 'Lookers Sports Bar', 'Chip \'n\' Tales']


foods = ['Baked Beans', 'Tuna', 'SPAM', 'Potted Meat', 'Canned Vegatables', 'M.R.E.',
         'Stale Pringles', 'Chef Boy-R-Dee', 'Bottled Water', 'Twinkies', 'Ding-Dongs', 'Rotel']


stash = []

hunger = 5
day_number = 0
raider_encounters = 0
food_ate = 0
buildings_looted = 0


start()

while True:

    hunger, day_number, raider_encounters, food_ate, buildings_looted = home_menu(hunger, day_number, raider_encounters, food_ate, buildings_looted)

    #print('hunger is ', hunger)
    #print('day is ', day_number)
    #print('raider count is', raider_encounters)
    #print('food ate is ', food_ate)
    #print('building looted is ', buildings_looted)

    

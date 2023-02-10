from pyfiglet import figlet_format
import sys
import time
from func_list import home_menu


def typewriter(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)



def start():
    print(figlet_format('    S C A V E N G E R', font='doom'))
    print(figlet_format('A TEXT GAME', font='chunky'))

    typewriter('Just another day in the wasteland...\nYou must SCAVENGE for food or DIE!!!\nYour stockpiles are low and raiders have entered your town.\nSave what you can and eat when you have to.\nSURVIVE AS LONG AS POSSIBLE!!!\n')


start()
home_menu()

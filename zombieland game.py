import sys
import time
import textwrap
import pickle
from classes import character
from classes import zombie 
from classes import hp_up1

zombie2= zombie("zombie king", 70, 50)
z=zombie("zom",10,30)
z2=zombie("zobla",45,30)
z1=zombie("cona",50,30)

chug_jug = hp_up1("{Chug Jug}")

gameMap = " _______________________________\n\
|\t\t\t\t|\n|\
\t     the lounge\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
_______________    ____________|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  \t\t|\n|\
  living room\t   | room 1\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
_______________|  |____________|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\troom 0\t\t|\n|\
\t\t\t\t|\n|\
\tstarting point\t\t|\n|_______________________________|"


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def exit_the_game():
    print("\n")
    print_slow("You are about to exit the game without save, do you want to save the game? # yes / no #\n")
    print("\n")
    exit_the_game_option = input("--->")
    while True:
        if exit_the_game_option == "yes":
            input("press enter to exit the game...")
            sys.exit(0)
        elif exit_the_game_option == "no":
            save() 


def save():
    save = open("save.txt", "wb")
    global char1 
    global chug_jug
    global inventory
    pickle.dump(char1, save)
    pickle.dump(inventory, save)
    pickle.dump(chug_jug, save)
    save.close()
    print ("\nGame has been saved!\n")
    input("press enter to go back...")
    alley()


def load():
    load = open("save.txt", "rb")
    global char1 
    global chug_jug
    global inventory
    char1 = pickle.load(load)
    inventory = pickle.load(load)
    chug_jug = pickle.load(load)
    print ("\nGame has been loaded!\n")
    room_0()


def first_screan():
    print_slow("welcome to \
the most adventure Zombieland game.\n\
you are about to be part of this game \
")
    print("\n")
    input("press enter to continue")
    print("\n")
    first_screan_option =input("Would like to play? # yes or no #\n--->")
    while True:
        if first_screan_option.lower() == "yes":
            print("good choose")
            main_menu()
            break
        elif first_screan_option.lower() == "no":
            sys.exit(0)
            break
        else:
            time.sleep(1)
            print("I think you did not choose one of the options!\n")
            time.sleep(1)
            print("please, choose # yes or no # \n")
            time.sleep(1)
            print("\n")
            first_screan_option =input("Would like to play?\n--->")
            continue


def main_menu():

    print_slow("choose one of the game option\n\
    1) start game\n\
    2) load game\n\
    3) about\n\
    4) exit")
    print("\n")
    main_menu_option = input("--->")
    while True:
        if main_menu_option == "1" or main_menu_option.lower() == "start" or main_menu_option.lower() == "start game":
            start()
            break
        elif main_menu_option == "2" or main_menu_option.lower() == "load game":
            load()   
            break
        elif main_menu_option == "3" or main_menu_option.lower() == "about":
            about()
            break
        elif main_menu_option == "4" or main_menu_option.lower()== "exit":
            print_slow("you do not have the courage to play this game\n")
            print_slow("come back when you are courage enough")
            time.sleep(2)
            sys.exit(0)
            break
        else:
            print("I think you did not choose one of the options!\n")
            time.sleep(1)
            print("please pick one of the above!\n")
            print_slow("choose one of the game option\n\
        1) start game\n\
        2) about\n\
        3) exit")
            print("\n")
            main_menu_option = input("--->")
            continue

def about():
    print_slow("In this game, there is a map that will be Showing wherever you go.\n\
         It will show where you are. \nThe map looks like this:")
    time.sleep(1)
    print("\n")
    print(gameMap)
    print("\n")
    time.sleep(1)
    print_slow("There is a drink colled # chug jug #; this drink will add 50 points\n\
    to your health; you need to look for it")
    print("\n")
    time.sleep(1)
    print_slow("When you start the game; you will start in room 0, you will be unarmed; you need to look for weapons.\n")
    print("\n")
    time.sleep(1)
    print_slow("You might be facing a zombie. Look after yourself.\n")
    print("\n")
    time.sleep(1)
    print_slow("!! Enjoy !!")
    print("\n")
    time.sleep(1)
    print_slow("press enter to go back to the main menu\n")
    print("\n")
    print_slow(input("--->"))
    time.sleep(1)
    main_menu()

def start():
    print("\n")
    print_slow("The story started when you end up here after a crazy night with guys,\n\
    you were in a drinking challenge, you had been drinking till you fell down.\n\
    then in your way back home you walked in the forest, and you find a house there,\n\
    and you ask yourself while you are Drunk: why don't I get in this house.\n\
    At that point you don't remember anything from that night you just woke up\n\
    in the middle of the night. \n  now try to survive from this house. ")
    time.sleep(1)
    print("\n")
    print("first choose the player name:")
    print("\n")
    x =input("Enter your name\n --->")
    global char1
    char1 = character(x)
    global chug_jug

    print("\n")
    print(f"great your player name is {char1.name}")
    print("\n")
    time.sleep(1)
    print("before start there are some tips to survive")
    time.sleep(1)
    print("\n")
    print_slow("to win this game you need to go to the lounge and there is an exit door there.")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("if I were you, I would check all rooms first before I got to the lounge.")
    print("\n")
    time.sleep(1)
    print("I would double check the rooms who knows it might be something new appear.")
    print("\n")
    time.sleep(1)
    print("now you are ready to start")
    print("\n")
    time.sleep(1)
    print("enjoy your adventure and meet me at the end see you later.")
    print("\n")
    print("you will start in room 0")
    print("\n")
    input("press enter to start")
    
    room_0()


def alley():
    print("\n")
    time.sleep(1)
    print_slow("you have exit the room")
    print("\n")
    print("where do you want to go: \n\
    1) room 0\n\
    2) room 1\n\
    3) living room\n\
    4) the lounge\n\
    5) save\n\
    6) exit the game")
    print("\n")
    alley_option = input("--->")
    while True:
        if alley_option == "1" or alley_option.lower() == "room 0":
            room_0()
            break
        elif alley_option == "2" or alley_option.lower() == "room 1":
            room_1()
            break
        elif alley_option == "3" or alley_option.lower() == "living room":
            living_room()
            break
        elif alley_option == "4" or alley_option.lower() == "the lounge":
            sure_the_lounge()
            break
        elif alley_option == "5" or alley_option.lower() == "save":
            save()
            continue
        elif alley_option == "6" or alley_option.lower() == "save and exit":
            sure = input("are you sure you want to exit # yes or no #")
            if sure == "yes":
                exit_the_game()
                break
            elif sure == "no":
                alley()
        else:
            print("I think you did not choose one of the options!\n")
            time.sleep(1)
            print("please pick one of the above!")
            print("\n")
            print("where do you want to go: \n\
        1) room 0\n\
        2) room 1\n\
        3) living room\n\
        4) the lounge\n\
        5) save\n\
        6) exit the game")
            alley_option = input("--->")
            continue

def look_around0():
    print_slow("I can't see anything useful to use")
    time.sleep(1)
    print("\n")
    print_slow("let's get out of the room ")
    time.sleep(1)
    print("\n")
    print_slow("press 1 to get out\n")
    look_around0_option = input("--->")
    while True:
        if look_around0_option == "1":
            alley()
            break
        else:
            alley()

def room_0():
    gameMap0 = " _______________________________\n\
|\t\t\t\t|\n|\
\t     the lounge\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
_______________    ____________|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  \t\t|\n|\
  living room\t   | room 1\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
_______________|  |____________|\n|\
\t\t\t\t|\n|\
\tyou are here\t\t|\n|\
\t\troom 0\t\t|\n|\
\t\t\t\t|\n|\
\tstarting point\t\t|\n|_______________________________|"

    print("\nyou are in room 0\n")
    print(gameMap0)
    print("what do you want to do?\n\
    1) look around\n\
    2) exit")
    room_0_option=input("--->")
    while True:
        if room_0_option =="1" or room_0_option.lower() == "look around" :
            look_around0()
            break
        elif room_0_option == "2" or room_0_option.lower() == "exit":
            alley()
            break
        else:
            print("what were you thinking when write this!\n")
            time.sleep(1)
            print("there are only 2 things to do, choose one of them!!")
            print("\n")
            print("what do you want to do?\n\
            1) look around\n\
            2) exit")
            room_0_option = input("--->")
            continue

inventory=[]

def look_around1():
    global chug_jug
    chug_jug = hp_up1("{Chug Jug}")
    L = [chug_jug.name]
    print("\nI can see something liquid in a jug")
    print("\n")
    time.sleep(1)
    print("I will read what it is written ")
    print_slow(f"it says: it is called {chug_jug.name}\n\
it will increase the hp with 50 points.")
    print("\n")
    print("do you want to take it and leave the room ? # yes or no #")
    print(" just leave it and leave the room\n")
    look_around1_option = input("--->")
    while True:
        if look_around1_option.lower() == "yes":
            if chug_jug in inventory:
                print(f"you have already had {chug_jug.name} in your inventory ")
                print (inventory)
                input("press enter...")
                alley()
                break
            else:
                inventory.append(chug_jug.name)
                L.remove(chug_jug.name)
                print_slow(f"you have {chug_jug.name}. your inventory now looks " )
                print (inventory)
                input("press enter...")
                alley()
                break
        else:
            print("you haven't had it, if you want it go in again")
            time.sleep(2)
            alley()
            break


def room_1():
    gameMap1 = " _______________________________\n\
|\t\t\t\t|\n|\
\t     the lounge\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
_______________    ____________|\n|\
\t\t|  |you are here|\n|\
\t\t|  |\t\t|\n|\
\t\t|  \t\t|\n|\
  living room\t   | room 1\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
_______________|  |____________|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\troom 0\t\t|\n|\
\t\t\t\t|\n|\
\tstarting point\t\t|\n|_______________________________|"
    print("\nyou are in room 1\n")
    print(gameMap1)
    print("what do you want to do?\n\
    1) look around\n\
    2) exit")
    room_1_option=input("--->")
    while True:
        if room_1_option =="1" or room_1_option.lower() == "look around" :
            look_around1()
            break
        elif room_1_option == "2" or room_1_option.lower() == "exit":
            alley()
            break
        else:
            print("what were you thinking when write this!")
            time.sleep(1)
            print("there are only 2 things to do, choose one of them!!")
            print("\n")
            print("what do you want to do?\n\
            1) look around\n\
            2) exit")
            room_1_option = input("--->")
            continue

def look_around2():
    S = ["Sword"]
    print_slow("\nohh!! finaly somthing I can fight with")
    print("\n")
    print_slow("I'll take that Sword with me")
    print("\n")
    print_slow("press yes to put it in your inventory and leave the room")
    
    look_around2_option = input("\n--->")
    while True:
        if look_around2_option.lower() == "yes":
            if "Sword"  in inventory:
                print("\nthe Sword is in your inventory\n ")
                print (inventory)
                input("press enter...")
                alley()
                break
            else:
                inventory.append(S[0])
                S.pop()
                print_slow("\nyou have { Sword } in your inventory now looks\n" )
                print (inventory)
                input("press enter...")
                alley()
                break
        else:
            print("you haven'y had it, if you want it go in again")
            time.sleep(2)
            alley()
            break


def living_room ():
    gameMap2 = " _______________________________\n\
|\t\t\t\t|\n|\
\t     the lounge\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
_______________    ____________|\n|\
\t\t|  |\t\t|\n|\
 you are here  |  |\t\t|\n|\
\t\t|  \t\t|\n|\
  living room\t   | room 1\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
_______________|  |____________|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\troom 0\t\t|\n|\
\t\t\t\t|\n|\
\tstarting point\t\t|\n|_______________________________|"
    print("\nyou are in the living room\n")
    print(gameMap2)
    print("\nwhat do you want to do?\n\
    1) look around\n\
    2) exit")
    living_room_option=input("--->")

    while True:
        if living_room_option =="1" or living_room_option.lower() == "look around" :
            look_around2()
            break
        elif living_room_option == "2" or living_room_option.lower() == "exit":
            alley()
            break
        else:
            print("what were you thinking when write this!")
            time.sleep(1)
            print("there are only 2 things to do, choose one of them!!")
            print("\n")
            print("what do you want to do?\n\
            1) look around\n\
            2) exit")
            living_room_option = input("--->")
            continue

def sure_the_lounge():
    print("\nare you sure you want to go to the lounge? ")
    time.sleep(1)
    print("\n")
    print("I would equipped the { sword } first and drink { Chug Jug } if I were you")
    print("\n")
    time.sleep(1)
    print("what is your choise?\n\
    1) equip\n\
    2) kick the door --> strong entry\n\
    3) quiet entry")
    print("\n")
    sure_the_lounge_option = input("--->")

    while True:
        if sure_the_lounge_option == "1" or sure_the_lounge_option.lower() == "equip":
            equip()
            break
        elif sure_the_lounge_option == "2" or sure_the_lounge_option.lower() == "kick the door":
            the_lounge_hard()
            break
        elif sure_the_lounge_option == "3" or sure_the_lounge_option.lower() == "quiet entry":
            the_lounge_quiet()
            break
        else:
            print("!! that's not one of the options !!")
            print("\n")
            print("chosse one of these\n\
            1) equip\n\
            2) kick the door\n\
            3) quiet entry")
            print("\n")
            sure_the_lounge_option = input("--->")
            continue

def equip():
    
    print("\nwhat do you want to have?\n\
    1) {Chug Jug}\n\
    2) Sword\n\
    3) Back")
    print("\n")
    equip_option = input("--->")
    while True:
        if equip_option == "1" or equip_option.lower() == "chug jug":
            if chug_jug.name not in inventory:
                print(f"{chug_jug.name} is not in the inventory ")
                equip()
                break
            else:
                char1.drink(chug_jug)
                print("your hp has increased to:")
                print(char1.hp)
                inventory.remove(chug_jug.name)
                equip()
                break
        elif equip_option == "2" or equip_option.lower() == "sword":
            if "Sword" not in inventory:
                print("Sword is not in the inventory ")
                equip()
                break
            else:
                char1.power +=10
                print(f"your power is increased to {char1.power} for attack.\nbecause you have sword in your hand")
                print(char1.power)
                inventory.remove("Sword")
                equip()
                break
        elif equip_option == "3" or equip_option.lower() == "back":
            sure_the_lounge()
            break
        else:
            equip()


def the_lounge_hard():
    global char1
    global z
    global z1
    global z2
    global zombie2

    gameMap4 = " _______________________________\n\
|\t\t\t\t|\n|\
\t     the lounge\t\t|\n|\
\t\t\t\t|\n|\
\tyou are here\t\t|\n|\
\t\t\t\t|\n|\
_______________    ____________|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  \t\t|\n|\
  living room\t   | room 1\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
_______________|  |____________|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\troom 0\t\t|\n|\
\t\t\t\t|\n|\
\tstarting point\t\t|\n|_______________________________|"
    print("you are in the lounge")
    print("\n")
    print(gameMap4)
    print("\n")
    print("you pissed off the zombies ")
    print("\n")
    print("sorry!!! you fucked up ")
    print("\n")
    print("all zombied are coming on you in once")
    time.sleep(3)
    char1 = zombie2.zattack(char1)
    print("\n")
    char1 = z.zattack(char1)
    print("\n")
    char1 = z2.zattack(char1)
    print("\n")
    char1 = z1.zattack(char1)
    print("\n")
    time.sleep(3)
    z= char1.pattack(z)
    print("\n")
    char1 = zombie2.zattack(char1)
    print("\n")
    char1 = z2.zattack(char1)
    print("\n")
    char1 = z1.zattack(char1)

    while True:
        if char1.hp <= 0:
            print("\n")
            print("you lost the game ")
            print("\n")
            print("Do you want to exit the game? # yes or no #")
            print("\n")
            y = input("--->")
            if y == "yes":
                input("press enter to exit")
                sys.exit(0)
                break
            elif y == "no":
                print("there is nothing to do with your body\n you will exit the game anyway")
                time.sleep(2)
                input("press enter to exit")
                sys.exit(0)
            break



def the_lounge_quiet():
    global char1
    global z
    global z1
    global z2
    global zombie2
    gameMap3 = " _______________________________\n\
|\t\t\t\t|\n|\
\t     the lounge\t\t|\n|\
\t\t\t\t|\n|\
\tyou are here\t\t|\n|\
\t\t\t\t|\n|\
_______________    ____________|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  \t\t|\n|\
  living room\t   | room 1\t|\n|\
\t\t|  |\t\t|\n|\
\t\t|  |\t\t|\n|\
_______________|  |____________|\n|\
\t\t\t\t|\n|\
\t\t\t\t|\n|\
\t\troom 0\t\t|\n|\
\t\t\t\t|\n|\
\tstarting point\t\t|\n|_______________________________|"
    print("you are in the lounge")
    print("\n")
    print(gameMap3)
    print("\n")
    print("there are some zombies!!")
    print("what do you want to do?\n\
    1) attack\n\
    2) run around looking for the door")
    the_loung_option=input("--->")
    while True:
        if the_loung_option =="1":
            z= char1.pattack(z)
            time.sleep(1)
            print("\n")
            print("good i have just killed the first")
            print("\n")
            time.sleep(1)
            z1= char1.pattack(z1)
            print("\n")
            print("the 2nd is down")
            print("\n")
            time.sleep(1)
            z2= char1.pattack(z2)
            print("\n")
            print("i think this is the last one")
            print("\n")
            print("\n")
            time.sleep(2)
            print("ohhhh no!!")
            print("\n")
            time.sleep(1)
            print("there is one more zombie,, it is huge")
            print("\n")
            time.sleep(1)
            zombie2 = char1.pattack(zombie2)
            print("\n")
            time.sleep(1)
            char1 = zombie2.zattack(char1)
            print("\n")
            time.sleep(1)
            zombie2 = char1.pattack(zombie2)
            print("\n")
            time.sleep(1)
            print("yeah!! I did it..> I'm free to get out of this place")
            print("finally I'm out. I love the sun")
            print("\n")
            input("press enter to exit --->")
            sys.exit(0)

        elif the_loung_option == "2":
            print_slow(".....>>....")
            print("\n")
            print("I can't run any longer. I need to fight the zombies")
            print("\n")
            time.sleep(2)
            z= char1.pattack(z)
            print("\n")
            print("good i have just killed the first")
            print("\n")
            time.sleep(2)
            z1= char1.pattack(z1)
            print("\n")
            print("the 2nd is down")
            print("\n")
            time.sleep(2)
            z2= char1.pattack(z2)
            print("\n")
            print("i think this is the last one")
            print("\n")
            print("\n")
            time.sleep(2)
            print("ohhhh no!!")
            print("\n")
            print("there is one more zombie,, it is huge")
            print("\n")
            time.sleep(2)
            zombie2 = char1.pattack(zombie2)
            print("\n")
            time.sleep(2)
            char1 = zombie2.zattack(char1)
            print("\n")
            time.sleep(2)
            zombie2 = char1.pattack(zombie2)
            print("\n")
            print("yeah!! I did it..> I'm free to get out of this place")
            print("finally I'm out. I love the sun")
            print("\n")
            input("press enter to exit")
            sys.exit(0)

        else: 
            print("this is not a viled input, please choose # 1 or 2 #")
            continue

first_screan()
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#importing
import time
from os import system, name 
import random


# %%
#Defining Function clear() 
#Clears the screen
def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


# %%
#Startup
print("Booting")
time.sleep(3)
print("Complete")
print("Testing for Y link...")
time.sleep(3)
print("Complete")
print("Entering the DeltaScape")
time.sleep(10)
clear()


# %%
#intro
print("choices are case sensitive")
print("Hey you! \nYou're finally awake. \nYou're the latest guy to appear at the Delta Dungeon.\nThe entrance is just ahead, enter inside and try to make it to the end")
choice = 0
while choice != "Y" or "N" :  
    choice = input("Enter the dungeon (Y/N)")
    if choice == "Y" :
        break
    elif choice == "N" :
        print("ok lol bye")
        print("Close the game") 
        while True:
            time.sleep(1)


# %%
#Pre game variables
mhealth = 20
chealth = mhealth
roomstraveled = 0
#Item Variables
#The higher the variale the more damage/defense
sword = 1
armor = 1
item = 0
#enemy's
monsters = ('skelly', 'zombie')


# %%
def fight():
    chealth = mhealth
    guard = 0
    ehealth = 2+roomstraveled
    edamage = roomstraveled - armor
    print(f"You engage the {monster}")
    strikeorder = random.randint(1,2)
    if strikeorder == 1:
        print(f"{monster} strikes you for {edamage} points of damage.")
        chealth -= edamage
    while chealth > 0 or ehealth > 0:  
        while True:
            print("Its your turn")
            choice = input("What would you like to do (Attack, Guard)")
            if choice == "Attack" :
                print(f"You attack the {monster} dealing {sword} points of damage")
                ehealth -= sword
                break
            if choice == "Guard" :
                print("You Protec")
                guard += 1
                break
        edamage = roomstraveled - armor - guard
        print(f"{monster} deals {edamage}")
        chealth -= edamage
        if chealth <= 0 :
            print("You died")
            print("Relaunch the game to try again")
            time.sleep(10)
            exit()
        if ehealth <= 0 :
            print(f"You defeated the {monster}")
            break

    
    

        

# %%
while True:
    room = random.randint(1,3)
    if room == 1 :
        print("\nYou enter a dank dungeon room covered in moss. It smells like the dead. There are skelletons chained up against the wall. \nThere is a chest in the room.")
        choice = input("Open the chest (Yes/No)")
        if choice == "Yes":
            print("You open the chest and...")
            item = random.randint(1,3)
            if item == 1:
                sword += 1
                if sword > 1:
                    print("You found a better sword")
                else:
                    print("You found a sword")
            
            if item == 2:
                armor += 1
                if armor > 1:
                    print("You found better armor")
                else:
                    print("You found armor")
            if item == 3:
                chealth = mhealth
                print("You found a health potion (HP fully restored)")
        else: 
            print('you walk past the chest and leave the room')
        roomstraveled += 1
    if room == 2 :
        monster = random.choice(monsters)
        print(f"\nYou enter a dank room with wet & shiny walls\nas you look around you spot a {monster}\nyou prepare to fight drawing your sword.")
        fight()
    if room == 3:
    	monster = random.choice(monsters)
    	print(f"You enter a room covered in weird neon colours, and with weed, the numbers 69 and 420, a penis, the American flag, a gun, a camera.\nWait is that a {monster}, get ready for a fight.")
        fight()

            


# %%




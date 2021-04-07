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
room = 0
proom = 0
#Item Variables
#The higher the variale the more damage/defense
sword = 1
armor = 0
item = 0
#enemy's
normalmonsters = ('skelly', 'zombie', 'Ghost', 'ERROR')


# %%
def fight():
    #Fixing stats
    global chealth
    
    
    #monster stats go here with
    mbonushealth = 0
    mbonusdamage = 0
    if monster == 'skelly':
    	mbonushealth = -1
    	mbonusdamage = 1
    if monster == 'corruptboss':
    	mbonusdamage = 2
    	mbonushealth = 2
    if monster == 'Ghost':
    	mbonusdamage = -1
    	mbonushealth = 5
    if monster == 'ERROR':
    	mbonusdamage = random.randint(1,5)
    	mbonushealth = random.randint(1,5)
    
    	
    	
    
    #calculatons
    guard = 0
    ehealth = 2 + roomstraveled + mbonushealth
    edamage = 1+ roomstraveled - armor + mbonusdamage
    #beginning of the actual fight
    print(f"You engage the {monster}")
    strikeorder = random.randint(1,2) #determines who goes first
    if strikeorder == 1:
        print(f"{monster} strikes you for {edamage} points of damage.")
        chealth -= edamage
    while chealth > 0 or ehealth > 0:  
        while True:
        		#players turn and appropriate dialog.
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
        if edamage < 1:
        	edamage = 1
        chealth -= edamage
        if chealth <= 0 :
            print("You died")
            print("Relaunch the game to try again")
            print(f'You made it {roomstraveled} rooms')
            time.sleep(10)
            exit()
        if ehealth <= 0 :
            print(f"You defeated the {monster}")
            break
	
    
    

        

# %%
while True:
    clear()
    while room == proom :
       room = random.randint(1,5) #picks random room
    
    
    if room == 1 :
        proom = 1
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
        proom=2
        monster = random.choice(normalmonsters)
        print(f"\nYou enter a dank room with wet & shiny walls\nas you look around you spot a {monster}\nyou prepare to fight drawing your sword.")
        fight()
        roomstraveled =+ 1
    if room == 3:
    	proom=3
    	monster = random.choice(normalmonsters)
    	print(f"You enter a room covered in weird neon colours, and with weed, the numbers 69 and 420, a penis, the American flag, a gun, a camera.\nWait is that a {monster}, get ready for a fight.")
    	fight()
    	roomstraveled =+ 1
    if room == 4:
    	proom =4
    	monster = 'corruptboss' #custom boss for this room
    	print('You enter a room covered in a purple and black checker pattern and before you stands a massive creature with black and purple fur, and it does not look happy to see a visitor.')
    	fight()
    	roomstraveled += 1
    if room == 5 :
    	proom=5
    	monster = random.choice(normalmonsters)
    	print(f'You enter a large gladitorial arena somehow and on the otherside of the arena is a {monster}')
    	fight()
    	print('due to your victory you recieve...')
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
    	roomstraveled += 1

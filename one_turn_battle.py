#This imports the random module, which is used for generating random numbers. The user is asked to enter a seed number to initialize the random number generator
import random
seed = int(input("Enter the seed to run the fight with: "))
random.random(seed)

#This part of the code is so we can get the input information about the attacker stats
attacker_hp = int(input("Enter the attacker's hp: "))
attacker_strength = int(input("Enter the attacker's strength: "))
attacker_accuracy = float(input("Enter the attacker's accuracy: ")) / 100
attacker_crit_chance = float(input("Enter the attacker's crit chance: ")) / 100
attacker_dodge_rate = float(input("Enter the attacker's dodge rate: ")) / 100

#This part of the code is so we can get the input information about the defender stats
defender_hp = int(input("Enter the defender's hp: "))
defender_strength = int(input("Enter the defender's strength: "))
defender_accuracy = float(input("Enter the defender's accuracy: ")) / 100
defender_crit_chance = float(input("Enter the defender's crit chance: ")) / 100
defender_dodge_rate = float(input("Enter the defender's dodge rate: ")) / 100
defender_guard = input("Is the defender guarding? Y for yes, n for no: ").lower() == 'y'

#This huge if else blocks of code is for the game logic based off the rules
#This if statement is to determine the outcome of the attackers turn
if random.random() < attacker_crit_chance:
    damage = attacker_strength + 1
    defender_hp -= damage
    print(f"attacker crits defender for {damage} points of damage")
else:
    #This part of the code is in the event the attack hits
    if random.random() < attacker_accuracy:
        #This part of the code is if the user dodges
        if random.random() < defender_dodge_rate:
            print("defender dodged attacker's attack")
        #This part of the code is to calculate the normal damage
        else:
            damage = random.randint(attacker_strength // 2, attacker_strength)
            defender_hp -= damage
            print(f"attacker hits defender for {damage} points of damage")
    #This part of the code is if the attacker misses
    else:
        print("attacker missed defender")
    #This part of the code is if the defender counter-attacks if the attacker missed or was dodged
    if defender_guard or random.random() < defender_accuracy:
        if random.random() < attacker_dodge_rate:
            print("attacker dodged defender's attack")
        else:
            if random.random() < defender_crit_chance:
                damage = defender_strength + 1
                attacker_hp -= damage
                print(f"defender crit attacker for {damage} points of damage")
            else:
                damage = random.randint(defender_strength // 2, defender_strength)
                attacker_hp -= damage
                print(f"defender hits attacker for {damage} points of damage")
#This part of the code is just the result of the battle
print(f"After fighting the attacker has {attacker_hp} hp left and the defender has {defender_hp} hp left")




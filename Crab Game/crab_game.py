
#Importing needed modules

import random, time, sys

def main():


    # displays intro text
    intro_text()

    # loop for if players choose to play again
    while True:

################## VARIABLES ##################

        # Health Variables
        player_max_health = 10

        player_health = 10

        kingcrab_health = 20

        #Damage variables

        crab_minimum_damage = 1
        crab_max_damage = 4

        sword_minimum_damage = 2
        sword_max_damage = 4

        bow_minimum_damage = 1
        bow_max_damage = 7

        falling_rock_minimum_damage = 1
        falling_rock_max_damage = 5

        bat_minimum_damge = 1
        bat_max_damage = 2

        berries_minimum_damge = 1
        berries_max_damge = 2

        #Healing variables

        healing_potions_healing_amount = 5

        berries_minimum_heal = 2
        berries_max_heal = 4

        # Variables for bow probability

        bow_weight = [0.2, 0.8]

        # Variables for starting items

        arrows = 3

        healing_potions_amount = random.randint(1,4)

        # Upgrade Variables 

        magic_sword_upgrade = 0

        magic_bow_upgrade = 0

        # Other Variables 

        random_event_chance = 3 # radomen events will have a 1 out of the "random_event_chance" chance of happening every round


################## Character Class ##################

        character_class = int(input ("Choose your class! \n(1) Knight - insreases your starting health to 17\n(2) Archer - gives you an extra arrow and decreases your miss odds to 10% \n(3) Alchemist - gives you 2 extra healing potions and allows you to see how many potions you have\n>"))
        
        character_class = class_var_convert(character_class)

        match character_class:

            case "knight": 
                player_health = 17
                player_max_health = 17
            case "archer": 
                arrows += 1
                bow_weight = [0.1, 0.9]
            case "alchemist": 
                healing_potions_amount += 2
            case "buddy":
                arrows = 10000
                healing_potions_amount = 10000
                player_health = 10000
                kingcrab_health = 10000


################## Gameplay Loop ##################
        while True:

            health_display(kingcrab_health, player_health)

            input()

            print ("The King Crab Attacks You!")

            input ()

            player_health -= random.randint(crab_minimum_damage, crab_max_damage)

            display_health(player_health, "player")

            input()

            if player_health < 1:
                print ("You died!")
                break

            action = int(input( 
            f"Would you like to? \n"
            f"(1) Use your sword \n"
            f"(2) Use your bow (You have {arrows} arrows left)\n"
            f"(3) Check your bag for a healing potion to drink "
            + (f"(You have {healing_potions_amount} potions left) " if character_class == "alchemist" else "")
            + "\n> "
            ))

################## Character Actions ##################

            match action:

                case 1:
                    print("You swing your sword and hit the King Crab!")
                    input()
                    kingcrab_health -= random_int_mod(sword_minimum_damage, sword_max_damage, magic_sword_upgrade)
                    display_health(kingcrab_health, "crab")
                    input()

                case 2:
                    if arrows >= 1 and arrow_shot_hit(bow_weight) == 1:
                        print("You shoot your bow and hit the King Crab!")
                        input()
                        kingcrab_health -= random_int_mod(bow_minimum_damage, bow_max_damage, magic_bow_upgrade)
                        display_health(kingcrab_health, "crab")
                        input()
                        arrows -= 1 
                        display_arrows_left(arrows)
                        

                    elif arrows >= 1:
                        print("You miss your shot!")
                        input()
                        arrows -= 1 
                        display_arrows_left(arrows)


                    else: print ("You are out of arrows.")

                    input()

                case 3: 
                    if healing_potions_amount >= 1:
                        
                        player_health += healing_potions_healing_amount

                        if player_health > player_max_health:
                            player_health = player_max_health

                        print (f"You find and drink a healing potion. Your Health is now {player_health}")
                        healing_potions_amount -= 1
                    
                    else: print("You reach into your bag to find that you are out of potions")
                    input()

                
            # checks if crab is dead
            if kingcrab_health < 1:
                print("THE CRAB IS DEAD!")
                break


################## Random Events ##################

            random_event_check = random.randint(1, random_event_chance)


            if random_event_check == 1:

                random_event_table = random.randint(1, 4)


            # Falling Rocks

                match random_event_table:

                    case 1:
                
                        typing_print("You see a few rocks falling from above.")
                        input()

                        falling_rocks_action = int(input("Do you: \n"
                            "(1) Jump out of the way\n"
                            "(2) Grab the crab so the rocks hit you both\n>"
                            ))
                        
                        if falling_rocks_action == 1:

                            typing_print("You jump out of the way and avoid taking any damage. You see that the crab was also able to avoid the rocks.\n")
                            input()

                        if falling_rocks_action == 2:

                            typing_print("The rocks hit both you and the Crab.\n")
                            input()

                            kingcrab_health -= random.randint(falling_rock_minimum_damage, falling_rock_max_damage)
                            display_health(kingcrab_health, "crab")
                            input()

                            player_health -= random.randint(falling_rock_minimum_damage, falling_rock_max_damage)

                            display_health(player_health, "player")
                            input()

                        if player_health < 1 and kingcrab_health < 1: 
                            typing_print ("Both you and the King Crab are crushed by rocks and die...\n")
                            break

                        elif player_health < 1:
                            typing_print ("You die from the impact of the rocks.\n")
                            break
                                
                        elif kingcrab_health < 1:
                            typing_print("The King Crab is killed from the impact and you win!\n")
                            break

                        else: continue

            # Swarm of bats attack
                    case 2:

                        typing_print ("You see a giant swarm of bats coming straight for you!\n")
                        input()

                        #Making this its own var is important becaue otherwise it can mess up the if statmetns 
                        bat_arrow_shot = arrow_shot_hit(bow_weight)


                        swarm_of_bats_action = int(input("Do you: \n"
                            "(1) Brace for impact\n"
                            "(2) Shoot an arrow atthem to try and scare them off \n>"
                            ))
                        
                        if swarm_of_bats_action == 2 and arrows > 0 and (bat_arrow_shot == 1 or character_class == "archer"):
                            typing_print("You see the swarm of bats coming towards you.\n")
                            input()

                            typing_print("You shoot an arrow at the bats and the swarm disperses.\n")
                            input()

                            arrows -= 1
                            display_arrows_left(arrows)
                            input()
                        
                        elif swarm_of_bats_action == 2 and bat_arrow_shot == 0 and arrows > 0 and healing_potions_amount > 0:

                            typing_print("You miss the bats!\n")
                            input()

                            typing_print("The bats swarm you and take a healing potion from your bag.\n")
                            healing_potions_amount -= 1
                            input()

                            arrows -= 1
                            display_arrows_left(arrows)
                            input()
                        
                        elif swarm_of_bats_action == 2 and bat_arrow_shot == 0 and arrows > 0 and healing_potions_amount < 1:
                            typing_print("You miss the bats!\n")
                            input()

                            typing_print("The swarm of bats attack you!\n")

                            player_health -= random.randint (bat_minimum_damge, bat_max_damage)
                            display_health(player_health, "player")
                            input()

                            #Checks if the player is dead
                            if player_health < 1: 
                                typing_print("The bats bite you to death (bad way to go)")
                                break

                            arrows -= 1
                            display_arrows_left(arrows)
                            input()

                        elif healing_potions_amount > 0 :
                            if swarm_of_bats_action == 2: print ("You are out of arrows"); input()

                            typing_print("The bats swarm you and take a healing potions from your bag.\n")
                            healing_potions_amount -= 1
                            input()

                        elif healing_potions_amount < 1:
                            if swarm_of_bats_action == 2: print ("You are out of arrows"); input()

                            typing_print("The swarm of bats attack you!\n")
                            input()

                            player_health -= random.randint (bat_minimum_damge, bat_max_damage)
                            display_health(player_health, "player")
                            input()
                            
                            #Checks if the player is dead
                            if player_health < 1: 
                                typing_print("The bats bite you to death (bad way to go)")
                                break

                        else: continue

            #berries
                if random_event_table == 3:

                    typing_print ("You see some interesting looking berries on the ground.")
                    input()

                    berries_action = int(input (
                        "Do you:\n"
                        "(1) Ingore the berries \n"
                        "(2) EAT THE BERRIES\n>"
                        ))
                    
                    if berries_action == 1:
                        typing_print("The berries feel very ingorned and go away.")
                        input()

                    elif berries_action == 2:
                        mystery_berry_outcome = random.randint(1, 4)

                        if mystery_berry_outcome == 1:
                            typing_print("You eat the berries and you start to feel sick.")
                            input()
                            
                            player_health -= random.randint(berries_minimum_damge, berries_max_damge)
                            display_health(player_health, "player")
                            input()

                            if player_health < 1: 
                                typing_print("You are poisoned to death by the berries")
                                break
                        
                        else:
                            typing_print("You eat the berries and feel a new sense of egenry!.")
                            input() 

                            player_health += random.randint(berries_minimum_heal, berries_max_heal)
                            display_health(player_health, "player")
                            input()


            # Something catches your eye
                if random_event_table == 4:

                    typing_print("Something on the ground catches your eye.")
                    input()

                    found_item_action = int(input(
                        "Do you: \n"
                        "(1) Ingore the item \n"
                        "(2) Investigate the item \n>"
                    ))
                    
                    if found_item_action ==2:

                        random_found_item = random.randint (1, 100)

            #RAT
                        if 21 > random_found_item:

                            typing_print("You try and get a closer look at the object only to discover it's a rat!\n")
                            input()
                            typing_print ("The rat jumps up and bites you before running away")
                            input()

                            player_health -= 1
                            display_health(player_health, "player")
                            input()

                            #checks if player is dead
                            if player_health < 1: 
                                typing_print("Turns out that tiny bite was enough to kill you...")
                                break
                
                # NOTHING 

                        elif 41 > random_found_item:

                            typing_print("After looking closer at the item, you discover that there was nothing there.\n")
                        
                # ARROW

                        elif 61 > random_found_item:

                            typing_print ("You find an arrow on the ground!\n")
                            input()

                            arrows += 1 

                            print(f"You now have {arrows} arrows.")
                            (input)

                # HEALING POTION

                        elif 81 > random_found_item:
                            typing_print ("You find a healing potion on the ground!\n")

                            healing_potions_amount += 1

                # MAGIC SWORD

                        elif 91 > random_found_item:
                            typing_print ("You find a Magic Sword on the ground! (+1 to all sword attacks)\n")

                            magic_sword_upgrade += 1

                #MAGIC BOW
                        
                        elif 101 > random_found_item:
                            typing_print ("You find a Magic Bow on the ground! (+1 to all bow attacks)\n")

                            magic_bow_upgrade += 1

################## PLAY AGAIN ##################

        play_again = input("Would you like to play again? (y/n)")
        play_again = play_again.lower()

        if play_again == "n":
            print("Thanks for playing")
            break

# This function coverts class ints into class strings so the rest of the code reads easier
def class_var_convert(character_class):
    match character_class: 

        case 1: character_class = "knight"
        case 2: character_class = "archer"
        case 3: character_class = "alchemist"

        #Dev Mode
        case 1984: character_class = "buddy"
    
    return character_class

#This function retunrs a random int with a modifier
def random_int_mod(min_amount, max_amount, modifier):

    random_value = random.randint(min_amount, max_amount) + modifier

    return random_value

#This function produces the slow typing text effect 
def typing_print(text, delay=0.025):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)

#This function takes a list with two numbers. The first number is the chance of missing and the second number is the chance of hitting
def arrow_shot_hit (bow_weight):
    return random.choices([0, 1], weights=bow_weight)[0]

#This function displays the intro text
def intro_text():
    typing_print ("You have been chosen by the people to kill the Evil King Crab!\n[PRESS ENTER]\n")
    input()

    typing_print("Your Weapons: \n")

    typing_print(f"Sword: Deals 2-4 Damage.\n")

    typing_print("Bow: Deals 1-7 but you have a 20% chance of missing, and you only get 3 arrows.\n")

    typing_print("Healing Potions: At the start of the fight you are randomy given between 1-4 healing potions in your bag. \nBut you don't know how many you have until you run out. Every healing potion heals 5 health.\n")

    input()

#This function displays the health of the crab and player every round
def health_display(kingcrab_health, player_health):
        typing_print("=====================================================\n")
        typing_print(f"King Crab's Health:{kingcrab_health}"+ " "*10 + f"Your Health:{player_health}   \n")


#This displayers current health. If owner == "crab", it will display it as the crab's health. If the ownser == "player" it'll display it as the player's health.
def display_health(health, owner):

    if owner == "crab":
        print(f"The King Crab's health is now {health}")

    elif owner == "player":
        print(f"Your health is now {health}")

#displays the current number of arrows the player has
def display_arrows_left(arrows):

    arrows_left_message = (f"You have {arrows} arrows left.")

    print (arrows_left_message)
    return arrows_left_message

#RUNS MAIN
if __name__ == "__main__":
    main()
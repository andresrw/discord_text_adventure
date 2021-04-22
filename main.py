#text based game based on hooligans
#create a "choose your character" thing where you can pick a
#discord user that has different stats
import random
import pprint


#player stats
total_points = 30
hp = 0
attack = 0
intelligence = 0
agility = 0
faith = 0
endurance = 0
escape_chance = 0

#Boss Stats
boss_hp = 0
boss_attack = 0
boss_intelligence = 0
boss_agility = 0
boss_faith = 0
boss_endurance = 0

def death(value):
    if hp <= 0:
        if value == "wulfer":
        print("You are trapped in the discord forever, slowly going insane\n"
              "Every person you see from now on looks like a Genshin character...")


#need to add the rest of the stats to the creator
def class_creator():
    global total_points
    global hp
    global intelligence
    global agility
    while total_points > 0:
        user_input = input("Which stat would you like to add points to? ")
        if user_input == "hp":
            print("The total amount of points you can spend is: " + str(total_points))
            hp = int(input("How many points do you wish to allocate into your HP? "))
            total_points = total_points - hp
            print("The remaining amount of points you can spend is " + str(total_points))
        elif user_input == "intelligence":
            print("The total amount of points you can spend is: " + str(total_points))
            intelligence = int(input("How many points do you wish to allocate into your Intelligence? "))
            total_points = total_points - intelligence
            print("The remaining amount of points you can spend is " + str(total_points))
        elif user_input == "agility":
            print("The total amount of points you can spend is: " + str(total_points))
            agility = int(input("How many points do you wish to allocate into your Agility? "))
            total_points = total_points - agility
            print("The remaining amount of points you can spend is " + str(total_points))
        elif total_points < 0:
            print("Oops! You ran out of points! Try again!")
            total_points = 30
        elif total_points = 0:
            print("You have spent all of you points")

create_class = input("Do you want to create you own class? Type yes or no: ")
if create_class == "yes":
    class_creator()
elif create_class == "no":
    #create a no option



def wulfer_boss():
    global boss_hp
    global boss_intelligence
    global boss_faith
    global boss_agility
    global boss_endurance
    global escape_chance
    global boss_attack
    global hp

    boss_hp = 5
    boss_attack = (boss_hp + boss_endurance) / 2
    boss_intelligence = 10
    boss_agility = 10
    boss_faith = 5
    boss_endurance = 7
    print("Hello, my name is Wulfer.")
    x = print("Do you want to see some Genshin fan art?")
    y = print("Do you want to donate for my Genshin rolls?")
    escape_chance = random.randint(0, agility)
    if escape_chance > boss_agility:
        print("Sorry Wulfer, I gotta go do something...else.")
        print("You disconnect from discord successfully.")
    elif escape_chance < boss_agility:
        print(x)
        print("You are not a degenerate weeb, so you obviously do not want to do this...here are your options: ")
        print("1. You decide to thrash out a Wulfer; the idea of being a weeb is disgusting so you swing at Wulfer's Face!") #hp
        print("2. You ask Wulfer if he has done his all of his homework yet, hoping he forgets about Genshin so you can escape!") #intelligence
        print("3. You tell Wulfer that God does not accept weebs into Heaven in an attempt to test his faith!") #faith
        print("4. You tell Wulfer yes, but you mute your microphone and walk away.") #endurance
        user_choice = int(input("Which # choice did you decide to try?"))

        #combat

        while boss_hp > 0:
            if user_choice == 1:
                while hp > 0:
                    hit_chance = random.randint(0, boss_agility)
                    if hit_chance > agility:
                        print("You missed!")
                        print("Wulfer bonks you on the head with some purple Genshin sword or something...")
                        damage = random.randint(1, boss_attack)
                        hp = hp - damage
                    elif hit_chance < agility:
                        print("You smacked Wulfer on the side of the head!")
                        damage = random.randint(1, attack)
                        boss_hp = boss_hp - damage
                else:
                    death("wulfer")
        else:
            print("Wulfer has seen the error of his ways,/n"
                  "he decides to better his live and stop being a weeb!")









def wabes_boss():
    global boss_hp
    global boss_intelligence
    global boss_faith
    global boss_agility
    global boss_endurance
    global escape_chance

    boss_hp = 5
    boss_intelligence = 10
    boss_agility = 5
    boss_faith = 15
    boss_endurance = 10
    print("Hello, my name is Wabes.")
    print("Come closer, let me show you your organs.")
    print("Let me show your the Kreb's cycle!")

import shutil
from tkinter import CENTER
from tracemalloc import stop
from colorama import Fore, Back, Style
import time
import random
import sys
from datetime import date

# This is to make the text appear like its being typed out
def slow_text(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice([
          0.001, 0.001, 0.001, 0.001, 0.001,
          0.001, 0.001, 0.001, 0.001, 0.001
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
cols, rows = shutil.get_terminal_size()
print(Fore.YELLOW +"")
slow_text("___                                           __                  "          .center(cols))
slow_text("\_ |__    ____ _______  ______  ____ _______ |  | __  ____ _______"           .center(cols))
slow_text("| __ \ _/ __ \/_  __ \/  ___/_/ __ \/_  __ \|  |/ /_/ __ \/_  __ \ "            .center(cols))
slow_text("| \_\ \/  ___/ |  | \/\___ \ \  ___/ |  | \/|    < \  ___/ |  | \/ "          .center(cols))
slow_text("|___  / \___  >|__|  /____  > \___  >|__|   |__|_ \ \___  >|__|  "       .center(cols))
slow_text("\/      \/            \/      \/             \/     \/     \/ "         .center(cols))






#the "Fore" is the colour you wish to put the link of code at, it will also do the rest of the code under it so you need to section this.
print(Fore.GREEN +"")
slow_text(".....................  <  <  GAME LOADING  >  >  ......................".center(cols))

slow_text(".....................  <  <  ------------  >  >  ......................".center(cols))


slow_text("Welcome to Berserker Your about to embark on a great and noble quest".center(cols))
slow_text("prepare yourself,sharpen your sword, gather your courage".center(cols))
slow_text("let us begin".center(cols))
print("                                                                                    ")
print("                                                                                     ")


#Players name function
player_name =  input(Fore.YELLOW +"What's your name adventurer ? : ".lower().strip().capitalize().center(cols))


while True:
    age = int(input(Fore.GREEN +f"Enter your age {player_name}: ".center(cols)))
    if age >= 16:
        print("                                                                                   ")
        input(Fore.YELLOW + "Press enter to start your adventure".center(cols))
        print("                                                         ")
        print(Fore.YELLOW +"")
        answer = input("You approach a stables do you get a horse or walk? Answer = (h/w): ".lower().strip().capitalize().center(cols))
        if answer == "h":
            print("")       
            print("                                                                                                                     {)                                                      ")
            print("                                                                                                                  c==//\                                                      ")
            print("                                                                                                             _-~~/-._|_|                                                          ")
            print("                                                                                                            /'_,/,   //'~~~\;;,                                                                         ")
            print("                                                                                                             `~  _( _||_..\ | ';;                                                                 ")
            print("                                                                                                               /'~|/ ~' `\<\>  ;                                                           ")
            print("                                                                                                              /  |      /  |    ")                                                              
            print(Fore.GREEN +"")
            slow_text("You get onto your horse and ride east towards Falador".center(cols))
            slow_text("after riding for over an hour you stop to give your horse a rest".center(cols))
            slow_text("Over your left shoulder you notice a goblin approaching...".center(cols))
            print(Fore.YELLOW +"")
            print("                                                                                                                 /(.-""-.)\                      ")
            print("                                                                                                             |\  \/      \/  /|               ")
            print("                                                                                                             | \ / =.  .= \ / |                    ")
            print("                                                                                                             \( \   o\/o   / )/                 ")
            print("                                                                                                              \_, '-/  \-' ,_/                      ")
            print("                                                                                                                /   \__/   \                       ")
            print("                                                                                                                \ \__/\__/ /                         ")
            print("                                                                                                              ___\ \|--|/ /___                  ")
            print("                                                                                                            /`    \      /    `\                    ")
            print("                                                                                                           |      '----'        |                     ") 
            print("                                                                                               ")                                   
            print(Fore.YELLOW +"                                                                                          ")
            answer =input("Do you kill the goblin or run away? Answer = (k/r) : ".lower().strip().capitalize().center(cols))
            if answer == "r":
                print(Fore.GREEN +"")
                slow_text("You decide to flee from the goblin leaving your sword and horse behind".center(cols))
                slow_text("you notice the goblin fast approaching and have nothing to defend yourself,".center(cols))
                print("")
                print(Fore.YELLOW +"")
                slow_text("Therefore brave adventurer you die..... R.I.P".center(cols))
                sys.exit()
            elif answer == "k":
                print("")
                slow_text(Fore.GREEN +"After killing your first goblin a wizard approach's you".center(cols))
                slow_text("he notices your injured during battle in order for him to heal you he asks for you to solve a riddle".center(cols))
                print("")
                print("                   .".center(cols))
                print ("        /^\     .  ".center(cols))
                print("    /\    V        ".center(cols))
                print("   /__\   I      O  o".center(cols))
                print("  //.. \  I     .    ".center(cols))
                print("  \].`[/  I          ".center(cols)) 
                print("  /l\/j\  (]    .  O  ".center(cols))
                print(" /. ~~ ,\/I          .".center(cols))
                print(" \L__j^\/I       o   ".center(cols))
                print("  \/--v}  I     o   .  ".center(cols))
                print("  |    |  I   _________".center(cols))
                print("  |    |  I c(`       ')o".center(cols))
                print("  |    l  I   \.     ,/".center(cols))
                print("_/j  L l\_!  _//^---^-\_".center(cols))
                print(Fore.YELLOW +"")
                answer = input ("What belongs to you but other people use it more than you (You use it to intoduce yourself) : ".capitalize().lower().strip().center(cols))
                if answer == "name":
                     
                    print(Fore.GREEN +"")
                    slow_text("The wizard jigs congratulating you on solving his riddle, he rewards you with 10 gold coins.".center(cols))
                    slow_text("The wizard then tells you that your wounds are to great and require further healing, he then asks you to go with him.".center(cols))
                    print("")
                    answer = input (Fore.YELLOW +"Do you go with the wizard? Answer = (y/n) :".capitalize().lower().strip().center(cols))

                elif answer != "your name"or "name" or "Your Name" or "yourname":
                    print("")
                    slow_text(Fore.GREEN +"You get the riddle wrong, the wizard shakes his head in disappointment, and vanishes.".center(cols))
                    slow_text("You are now bleeding out.... This is where your life ends".center(cols))
                    sys.exit()
                

                    

                    
                while True:
                    if answer == "y":
                        print(Fore.GREEN +"")
                        slow_text ("The wizard casts a spell on you, which puts you to sleep".center(cols))
                        slow_text ("You then wake up in the wizards tower, you hear a convocation in which the wizard is congratulated on bringing you back alive".center(cols))
                        slow_text("The goblin notices your awake and you notice things around you are very strange".center(cols))
                        
                    elif answer != "n":
                        print(Fore.GREEN +"")
                        slow_text("The wizard shakes his head in disappointment, and vanishes.".center(cols))
                        slow_text("You are now bleeding out and require healing.".center(cols))
                        slow_text("You wonder and fall down..... your adventure ends here".center(cols))
                        sys.exit()

                    while True:
                        print(Fore.YELLOW +"")

                        answer = input("You grab the nearest weapon to you, which in this case is a knife & mystery item. Answer = (k/mi) : ".capitalize().lower().strip().center(cols))
                        if answer == "k "or" mi": 
                            print(Fore.GREEN +"")
                            slow_text("You pick the item off the table, you slowly stand to your feet asking, WHAT IS GOING ON HERE?!".center(cols))
                            slow_text ("The goblin confronts the wizard and says YOU SAID HE WOULD BE ASLEEP".center(cols))
                            slow_text("taking advantage of the confusion you deal a fatal blow to the wizard using the item in hand, and you hold the goblin hostage.".center(cols))
                            slow_text("You integrate the goblin to find out where his leader is, he then tells you he is required to open the secret door to gain access to the leader.".center(cols))
                            print("")

                            answer = input(Fore.YELLOW + "Do you take the goblin with you? Answer = (y/n) : ".capitalize().lower().strip().center(cols))
                            if answer == "y":
                                print(Fore.GREEN +"")
                                slow_text("You go with the goblin to the secret door, as the goblin opens the door".center(cols))
                                slow_text("his leader appears and tears apart the goblin which opened the door you are now faced with the goblin leader.".center(cols))

                            elif answer =="n":
                                slow_text("You don't go with the goblin after you turn around to walk away".center(cols))
                                slow_text("the goblin grabs his spear and pierces it through your chest.You bleed out and die.".center(cols))
                                sys.exit()
                                
                            print("")
                                                 
             
                            print("")

                            answer = input(Fore.YELLOW + "Do you attack the goblin leader or do you run? Answer = (a/r) : ".capitalize().lower().strip().center(cols))
                            if answer == "a":
                                    print(Fore.GREEN +"")
                                    slow_text("You fight the goblin leader, but then he strikes you down loosing your weapon you now have nothing to attack him with".center(cols))
                                    slow_text("You look around to try and find a weapon, lucky enough you find a old rusty sword in the dirt".center(cols))
                                    slow_text("you pick it up as the goblin leader approaches you he throws his second blow at you which Misses".center(cols))
                                    slow_text("you then retaliate back dealing a blow to the goblin leader.".center(cols))
                                    slow_text("he falls to his knees, while bleeding you finish him off by putting the sword through his heart.")
                                    print(Fore.YELLOW +"")
                                    slow_text("Congratulations you killed the Goblin Leader ".center(cols))
                                    slow_text("you have completed the game!".center(cols))
                                    slow_text(" ______________________________________________________".center(cols))
                                    slow_text("   _____          __  __ ______    ______      ________ _____  ".center(cols))
                                    slow_text("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ".center(cols))
                                    slow_text(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |".center(cols))
                                    slow_text(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ".center(cols))
                                    slow_text(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ".center(cols))
                                    slow_text("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ".center(cols))
                                    print(" ______________________________________________________".center(cols))
                                    sys.exit()
                        
                            elif answer == "r":
                                    print(Fore.GREEN +"")
                                    slow_text ("As you try to run away from the goblin leader".center(cols))
                                    slow_text("he throws a axe which hits you in the head.You instantly die......R.I.P".center(cols))   
                            sys.exit()
                 
                            
                                    
                                                                   









        #Walking path

        elif answer == "w": 
            print(Fore.YELLOW +"                                                                  ".center(cols))
            print("                                                                                                           ,^.                   ")
            print("                                                                                                           |||                    ") 
            print("                                                                                                           |||       _T_           ")
            print("                                                                                                           |||   .-.[:|:].-.       ")
            print("                                                                                                           ===_ /\|   '   |/       ")   
            print("                                                                                                           E]_|\/ \--|-|''''|      ")
            print("                                                                                                           O  `'  '=[:]| A  |      ")
            print("                                                                                                                 /####|  P |       ")
            print("                                                                                                                /#####`.__.'       ")
            print("                                                                                                                / \/###\/\       ")
            print("                                                                                                                | \     / |       ")
            print("                                                                                                                | |     | |       ")
            print("                                                                                                              <####)     (####>      ")

            print(Fore.GREEN +"")
            slow_text("You decided to walk east towards Falador, ".center(cols))
            slow_text("after walking for over an hour you stop to give your legs a rest.".center(cols))
            slow_text("Over your left shoulder you notice a goblin approaching...".center(cols))


            print(Fore.RED +"")
            print("                                                                                                                 /(.-""-.)\                      ")
            print("                                                                                                             |\  \/      \/  /|               ")
            print("                                                                                                             | \ / =.  .= \ / |                    ")
            print("                                                                                                             \( \   o\/o   / )/                 ")
            print("                                                                                                              \_, '-/  \-' ,_/                      ")
            print("                                                                                                                /   \__/   \                       ")
            print("                                                                                                                \ \__/\__/ /                         ")
            print("                                                                                                              ___\ \|--|/ /___                  ")
            print("                                                                                                            /`    \      /    `\                    ")
            print("                                                                                                           |      '----'        |                     ") 


        answer =input("Do you kill the goblin or run away? Answer = (k/r) : ".capitalize().lower().strip().center(cols))
        if answer == "r":
                print(Fore.GREEN +"")
                slow_text("You decide to flee from the goblin leaving your sword and horse behind".center(cols))
                slow_text("you notice the goblin fast approaching and have nothing to defend yourself,".center(cols))
                print("")
                print(Fore.RED +"")
                slow_text("Therefore brave adventurer you die..... R.I.P".center(cols))
        elif answer == "k":
                print(Fore.GREEN +"")
                slow_text("After killing your first goblin a wizard approach's you".center(cols))
                slow_text("he notices your injured during battle in order for him to heal you he asks for you to solve a riddle".center(cols))
                print(Fore.YELLOW +"")

                print("                   .".center(cols))
                print ("        /^\     .  ".center(cols))
                print("    /\    V        ".center(cols))
                print("   /__\   I      O  o".center(cols))
                print("  //.. \  I     .    ".center(cols))
                print("  \].`[/  I          ".center(cols)) 
                print("  /l\/j\  (]    .  O  ".center(cols))
                print(" /. ~~ ,\/I          .".center(cols))
                print(" \L__j^\/I       o   ".center(cols))
                print("  \/--v}  I     o   .  ".center(cols))
                print("  |    |  I   _________".center(cols))
                print("  |    |  I c(`       ')o".center(cols))
                print("  |    l  I   \.     ,/".center(cols))
                print("_/j  L l\_!  _//^---^-\_".center(cols))
                print(Fore.RED +"")
                answer = input ("What belongs to you but other people use it more than you (You use it to intoduce yourself) : ".capitalize().lower().strip().center(cols))
                if answer == "name":
                     
                    print(Fore.GREEN +"")
                    slow_text("The wizard jigs congratulating you on solving his riddle, he rewards you with 10 gold coins.".center(cols))
                    slow_text("The wizard then tells you that your wounds are to great and require further healing, he then asks you to go with him.".center(cols))
                    print("                                                                         ")
                    answer = input (Fore.RED +"Do you go with the wizard? Answer = (y/n) :".capitalize().lower().strip().center(cols))

                elif answer != "your name"or "name" or "Your Name" or "yourname":
                    print(Fore.YELLOW +"")
                    slow_text("You get the riddle wrong, the wizard shakes his head in disappointment, and vanishes.".center(cols))
                    slow_text("You are now bleeding out.... This is where your life ends adventurer......R.I.P".center(cols))
                    sys.exit()
                

                    

                    
                while True:
                    if answer == "y":
                        print("                                                ")
                        slow_text (Fore.GREEN +"The wizard casts a spell on you, which puts you to sleep".center(cols))
                        slow_text ("You then wake up in the wizards tower, you hear a convocation in which the wizard is congratulated on bringing you back alive".center(cols))
                        slow_text("The goblin notices your awake and you notice things around you are very strange".center(cols))
                        
                    elif answer == "No":
                        slow_text("The wizard shakes his head in disappointment, and vanishes.".center(cols))
                        slow_text("You are now bleeding out and require healing.".center(cols))
                        slow_text("You wonder and fall down..... your adventure ends here".center(cols))
                        sys.exit()

                    while True:
                        print("")

                        answer = input(Fore.RED + "You grab the nearest weapon to you, which in this case is a knife & mystery item. Answer = (k/mi) : ".capitalize().lower().strip().center(cols))
                        if answer != "k "or" mi":
                            slow_text(Fore.GREEN +"You pick the item off the table, you slowly stand to your feet asking, WHAT IS GOING ON HERE?!".center(cols))
                            slow_text ("The goblin confronts the wizard and says YOU SAID HE WOULD BE ASLEEP".center(cols))
                            slow_text("taking advantage of the confusion you deal a fatal blow to the wizard using the item in hand, and you hold the goblin hostage.".center(cols))
                            slow_text("You integrate the goblin to find out where his leader is, he then tells you he is required to open the secret door to gain access to the leader.".center(cols))
                            print("")

                            answer = input(Fore.RED + "Do you take the goblin with you? Answer = (y/n) : ".capitalize().lower().strip().center(cols))
                            if answer == "y":
                                print(Fore.GREEN +"")
                                slow_text("You go with the goblin to the secret door, as the goblin opens the door".center(cols))
                                slow_text("his leader appears and tears apart the goblin which opened the door you are now faced with the goblin leader.".center(cols))
                                print("")

                            elif answer !="n":
                                slow_text("You don't go with the goblin after you turn around to walk away".center(cols))
                                slow_text("the goblin grabs his spear and pierces it through your chest.You bleed out and die.".center(cols))
                                sys.exit()
                                
                            print("")
                                                 
             
                            print("")

                            answer = input(Fore.RED + "Do you attack or do you run? Answer = (a/r) : ".capitalize().lower().strip().center(cols))
                            if answer == "a":
                                    print(Fore.GREEN +"")
                                    slow_text("You fight the goblin leader, but then he strikes you down loosing your weapon you now have nothing to attack him with".center(cols))
                                    slow_text("You look around to try and find a weapon, lucky enough you find a old rusty sword in the dirt".center(cols))
                                    slow_text("you pick it up as the goblin leader approaches you he throws his second blow at you which misses".center(cols))
                                    slow_text("you then retaliate back dealing a blow to the goblin leader.".center(cols))
                                    slow_text("he falls to his knees, while bleeding you finish him off by putting the sword through his heart.".center(cols))
                                    print(Fore.YELLOW +"")
                                    slow_text("Congratulations you kill the Goblin Leader!  ".center(cols)) 
                                    slow_text("you have completed the game!".center(cols))
                                    print(Fore.GREEN +"")
                                    slow_text(" ______________________________________________________".center(cols))
                                    slow_text("   _____          __  __ ______    ______      ________ _____  ".center(cols))
                                    slow_text("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ".center(cols))
                                    slow_text(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |".center(cols))
                                    slow_text(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ".center(cols))
                                    slow_text(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ".center(cols))
                                    slow_text("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ".center(cols))
                                    print(" ______________________________________________________".center(cols))
                                    sys.exit()
                        
                            elif answer == "r":
                                    slow_text ("As you try to run away from the goblin leader".center(cols))
                                    slow_text("he throws a axe which hits you in the head.You instantly die".center(cols))   
                            sys.exit()
    elif age <= 16:
        print("Your Too Young For This Game")
        break




    else:
        print("Unknow Command")
        sys.exit()

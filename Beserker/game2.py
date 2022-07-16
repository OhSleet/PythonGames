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
          0.005, 0.005, 0.005, 0.005, 0.005,
          0.005, 0.005, 0.005, 0.005, 0.005
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)


slow_text(Fore.YELLOW +"            ___.                                          __                                ")
slow_text("            \_ |__    ____ _______  ______  ____ _______ |  | __  ____ _______              ")
slow_text("             | __ \ _/ __ \/_  __ \/  ___/_/ __ \/_  __ \|  |/ /_/ __ \/_  __ \         ")
slow_text("             | \_\ \/  ___/ |  | \/\___ \ \  ___/ |  | \/|    < \  ___/ |  | \/             ")
slow_text("             |___  / \___  >|__|  /____  > \___  >|__|   |__|_ \ \___  >|__|                ")
slow_text("              \/      \/            \/      \/             \/     \/     \/ ")






#the "Fore" is the colour you wish to put the link of code at, it will also do the rest of the code under it so you need to section this.
slow_text(Fore.GREEN +"        .....................  <  <  GAME LOADING  >  >  ......................")

slow_text("        .....................  <  <  ------------  >  >  ......................")


slow_text("          Welcome to Berserker Your about to embark on a great and noble quest")
slow_text("                  prepare yourself,sharpen your sword, gather your courage")
slow_text("                                       let us begin")
print("                                                                                    ")
print("                                                                                     ")


#Players name function
player_name =  input(Fore.YELLOW +"What's your name adventurer ? : ")

while True:
    age = int(input(Fore.GREEN +f"Enter your age {player_name}: "))
    if age >= 16:
        print("                                                                                   ")
        input(Fore.YELLOW + "Press enter to continue.....")
        print("                                                         ")

        answer = input(Fore.YELLOW + "                     You approach a stables do you get a horse or walk? : ")
        if answer == "horse":
            print("                                                                                              ")       
            print("                               {)                           {)                                                      ")
            print("                            c==//\                       c==//\                                                      ")
            print("                       _-~~/-._|_|                  _-~~/-._|_|                                                          ")
            print("                      /'_,/,   //'~~~\;;,          /'_,/,   //'~~~\;;,                                                                         ")
            print("                       `~  _( _||_..\ | ';;         `~  _( _||_..\ | ';;                                                                 ")
            print("                           /'~|/ ~' `\<\>  ;            /'~|/ ~' `\<\>  ;                                                           ")
            print("                          /  |      /  |               /  |      /  |                                                                    ")
            slow_text(Fore.GREEN +"                               You get onto your horse and ride east towards Falador")
            slow_text(Fore.GREEN +"                          after riding for over an hour you stop to give your horse a rest")
            slow_text(Fore.GREEN +"                               Over your left shoulder you notice a goblin approaching...")
            print("      ")
            print(Fore.YELLOW +"                                                       ,      ,                        ")
            print("                                                       /(.-""-.)\                      ")
            print("                                                   |\  \/      \/  /|               ")
            print("                                                   | \ / =.  .= \ / |                    ")
            print("                                                   \( \   o\/o   / )/                 ")
            print("                                                    \_, '-/  \-' ,_/                      ")
            print("                                                      /   \__/   \                       ")
            print("                                                      \ \__/\__/ /                         ")
            print("                                                    ___\ \|--|/ /___                  ")
            print("                                                  /`    \      /    `\                    ")
            print("                                                 |      '----'        |                     ") 
            print("                                                                                               ")
            print(Fore.YELLOW +"                                                                                          ")
            answer =input("                                      Do you kill the goblin or run away?  (Kill/Run) : ")
            if answer == "run":
                slow_text(Fore.GREEN +"                                     You decide to flee from the goblin and and leave your sword behind")
                slow_text("                             you notice the goblin fast approaching and you cannot find your sword to defend yourself,")
                print("                                                                            ")
                print("                                                                        ")
                slow_text(Fore.YELLOW +"                                     Therefore brave adventurer you die..... R.I.P")
            elif answer == "kill":
                print("                                                                ")
                slow_text(Fore.GREEN +"After killing your first goblin a wizard approach's you")
                slow_text("he notices your injured during battle in order for him to heal you he asks for you to solve a riddle")
                print("                                                            ")
                answer = input (Fore.YELLOW +"What belongs to you but other people use it more than you (You use it to intoduce yourself) : ")
                if answer == "your name":
                     
                    print("                                                                     ")
                    slow_text(Fore.GREEN +"The wizard jigs congratulating you on solving his riddle, he rewards you with 10 gold coins.")
                    slow_text("The wizard then tells you that your wounds are to great and require further healing, he then asks you to go with him.")
                    print("                                                                         ")
                    answer = input (Fore.YELLOW +"Do you go with the wizard? (Yes/No) :")

                elif answer != "your name..":
                    print(                                )
                    slow_text(Fore.GREEN +"You get the riddle wrong, the wizard shakes his head in disappointment, and vanishes.")
                    slow_text("You are now bleeding out.... This is where your life ends")
                    sys.exit()
                

                    

                    
                while True:
                    if answer == "yes":
                        print("                                                ")
                        slow_text (Fore.GREEN +"The wizard casts a spell on you, which puts you to sleep")
                        slow_text ("You then wake up in the wizards tower, you hear a convocation in which the wizard is congratulated on bringing you back alive")
                        slow_text("The goblin notices your awake and you notice things around you are very strange")
                        
                    elif answer == "no":
                        slow_text(Fore.GREEN +"The wizard shakes his head in disappointment, and vanishes.")
                        slow_text("You are now bleeding out and require healing.")
                        slow_text("You wonder and fall down..... your adventure ends here")
                        sys.exit()

                    while True:
                        print("                                                       ")

                        answer = input(Fore.YELLOW + "You grab the nearest weapon to you which in this case is (Knife / Mystery Item) : ")
                        if answer == "knife "or" Mystery Item":
                            print("                                                                 ")
                            slow_text(Fore.GREEN + "You pick the item off the table, you slowly stand to your feet asking, what is going on here?")
                            slow_text ("The goblin confronts the wizard and says YOU SAID HE WOULD BE ASLEEP")
                            slow_text("taking advantage of the confusion you deal a fatal blow to the wizard using the item in hand, and you hold the goblin hostage.")
                            slow_text("You integrate the goblin to find out where his leader is, he then tells you he is required to open the secret door to gain access to the leader.")
                            print("                                                          ")

                            answer = input(Fore.YELLOW + "Do you take the goblin with you? (Yes/No) : ")
                            if answer == "yes":
                                slow_text(Fore.GREEN +"You go with the goblin to the secret door, as the goblin opens the door")
                                slow_text("his leader appears and tears apart the goblin which opened the door you are now faced with the goblin leader.")

                            elif answer =="no":
                                slow_text("You don't go with the goblin after you turn around to walk away")
                                slow_text("the goblin grabs his spear and pierces it through your chest.You bleed out and die.")
                                sys.exit()
                                
                            print("                                                                                     ")
                                                 
             
                            print("                                                               ")

                            answer = input(Fore.YELLOW + "Do you attack or do you run?(Attack/Run) : ")
                            if answer == "attack":
                                    print("                                                                      ")
                                    slow_text(Fore.GREEN +"You fight the goblin leader, but then realized you have nothing to attack him with.....")
                                    slow_text("You look around to try and find a weapon and find a old rusty sword in the dirt")
                                    slow_text("you pick it up as the goblin leader approaches you he throws his first blow at you which Misses")
                                    slow_text("you then retaliate back dealing a killing blow to the goblin leader.")
                                    print("                                                              ")
                                    slow_text(Fore.YELLOW +"Congratulations you complete the game!  ") 
                                    print(" ______________________________________________________")
                        
                            elif answer == "run":
                                    slow_text (Fore.GREEN +"As you try to run away from the goblin leader")
                                    slow_text("he throws a axe which hits you in the head.You instantly die")   
                            sys.exit()
                 
                            
                                    
                                                                   











        elif answer == "walk": 
            print(Fore.YELLOW +"                                                                  ")
            print('                                      00                      ')
            print("                                     dMMP                        ")
            print("                                     dMMM'                        ")
            print("                                     \MM/                 ")  
            print("                                     dMMm.                        ")
            print("                                    dMMP'_\---.                   ")
            print("                                   _| _  p ;88;`.                 ")
            print("                                 ,db; p >  ;8P|  `.                   ")
            print("                                (``T8b,__,'dP |   |               ")
            print("                                |   `Y8b..dP  ;_  |               ")
            print("                                |    |`T88P_ /  `\;                   ")
            print("                              :_.-~|d8P'`Y/    /                  ")
            print("                                 \_   TP    ;   7`\               ")
            print("                     ,,__        >   `._  /'  /   `\_                 ")
            print('                      `._ -----~~~~------|`\; ;     , \                ')
            print("                         ----~~~~~~-~~~\               ")
            print("                                ;--..._     .-'-._     ;                  ")
            print('                                /      /`~~"'   ,'`\_ /         ')
            print("                               ;_    /'        /    ,/                ")
            print("                               | `~-l         ;    /              ")  
            print("                               `\    ;       /\.._|                   ")
            print("                                 \    \      \     \                  ")
            print("                                /`---';      `----'                   ")
            print("                                (     /                           ")
            print("                                 `---'                        ")
            print("                                                                 ")
            slow_text(Fore.GREEN +"                     You decided to walk east towards Falador, ")
            slow_text("           after walking for over an hour you stop to give your legs a rest.")
            slow_text("             Over your left shoulder you notice a goblin approaching...")











        

            print(Fore.RED +"                                                       ,      ,                        ")
            print("                                                       /(.-""-.)\                      ")
            print("                                                   |\  \/      \/  /|               ")
            print("                                                   | \ / =.  .= \ / |                    ")
            print("                                                   \( \   o\/o   / )/                 ")
            print("                                                    \_, '-/  \-' ,_/                      ")
            print("                                                      /   \__/   \                       ")
            print("                                                      \ \__/\__/ /                         ")
            print("                                                    ___\ \|--|/ /___                  ")
            print("                                                  /`    \      /    `\                    ")
            print("                                                 |      '----'        |                     ") 






        answer =input("                                      Do you kill the goblin or run away?  (Kill/Run) : ")
        if answer == "run":
                slow_text(Fore.GREEN +"                                     You decide to flee from the goblin and and leave your sword behind")
                slow_text("                             you notice the goblin fast approaching and you cannot find your sword to defend yourself,")
                print("                                                                            ")
                print("                                                                        ")
                slow_text(Fore.RED +"                                     Therefore brave adventurer you die..... R.I.P")
        elif answer == "kill":
                print("                                                                ")
                slow_text(Fore.GREEN +"After killing your first goblin a wizard approach's you")
                slow_text("he notices your injured during battle in order for him to heal you he asks for you to solve a riddle")
                print("                                                            ")
                answer = input (Fore.RED +"What belongs to you but other people use it more than you (You use it to intoduce yourself) : ")
                if answer == "your name":
                     
                    print("                                                                     ")
                    slow_text(Fore.GREEN +"The wizard jigs congratulating you on solving his riddle, he rewards you with 10 gold coins.")
                    slow_text("The wizard then tells you that your wounds are to great and require further healing, he then asks you to go with him.")
                    print("                                                                         ")
                    answer = input (Fore.RED +"Do you go with the wizard? (Yes/No) :")

                elif answer != "your name..":
                    print(                                )
                    slow_text(Fore.GREEN +"You get the riddle wrong, the wizard shakes his head in disappointment, and vanishes.")
                    slow_text("You are now bleeding out.... This is where your life ends")
                    sys.exit()
                

                    

                    
                while True:
                    if answer == "yes":
                        print("                                                ")
                        slow_text (Fore.GREEN +"The wizard casts a spell on you, which puts you to sleep")
                        slow_text ("You then wake up in the wizards tower, you hear a convocation in which the wizard is congratulated on bringing you back alive")
                        slow_text("The goblin notices your awake and you notice things around you are very strange")
                        
                    elif answer == "no":
                        slow_text("The wizard shakes his head in disappointment, and vanishes.")
                        slow_text("You are now bleeding out and require healing.")
                        slow_text("You wonder and fall down..... your adventure ends here")
                        sys.exit()

                    while True:
                        print("                                                       ")

                        answer = input(Fore.RED + "You grab the nearest weapon to you which in this case is (Knife / Mystery Item) : ")
                        if answer == "knife "or" Mystery Item":
                            slow_text(Fore.GREEN +"You pick the item off the table, you slowly stand to your feet asking, what is going on here?")
                            slow_text ("The goblin confronts the wizard and says YOU SAID HE WOULD BE ASLEEP")
                            slow_text("taking advantage of the confusion you deal a fatal blow to the wizard using the item in hand, and you hold the goblin hostage.")
                            slow_text("You integrate the goblin to find out where his leader is, he then tells you he is required to open the secret door to gain access to the leader.")
                            print("                                                             ")

                            answer = input(Fore.RED + "Do you take the goblin with you? (Yes/No) : ")
                            if answer == "yes":
                                slow_text(Fore.GREEN +"You go with the goblin to the secret door, as the goblin opens the door")
                                slow_text("his leader appears and tears apart the goblin which opened the door you are now faced with the goblin leader.")
                                print("                                                                                 ")

                            elif answer =="no":
                                slow_text("You don't go with the goblin after you turn around to walk away")
                                slow_text("the goblin grabs his spear and pierces it through your chest.You bleed out and die.")
                                sys.exit()
                                
                            print("                                                                                     ")
                                                 
             
                            print("                                                               ")

                            answer = input(Fore.RED + "Do you attack or do you run?(Attack/Run) : ")
                            if answer == "attack":
                                    print("                                                                      ")
                                    slow_text(Fore.GREEN + "You fight the goblin leader, but then realized you have nothing to attack him with.....")
                                    slow_text("You look around to try and find a weapon and find a old rusty sword in the dirt")
                                    slow_text("you pick it up as the goblin leader approaches you he throws his first blow at you which Misses")
                                    slow_text("you then retaliate back dealing a killing blow to the goblin leader.")
                                    print("                                                              ")
                                    slow_text(Fore.YELLOW +"Congratulations you complete the game!  ") 
                        
                            elif answer == "run":
                                    slow_text ("As you try to run away from the goblin leader")
                                    slow_text("he throws a axe which hits you in the head.You instantly die")   
                            sys.exit()












    
    elif age <= 16:
        print("Your Too Young For This Game")
    break




    
    

    
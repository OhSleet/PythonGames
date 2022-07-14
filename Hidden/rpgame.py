# ##......................................................................
# //.HHHH...HHHH.HIIII.DDDDDDDDD....DDDDDDDDD....EEEEEEEEEEE.ENNN...NNNN..
# //.HHHH...HHHH.HIIII.DDDDDDDDDD...DDDDDDDDDD...EEEEEEEEEEE.ENNNN..NNNN..
# //.HHHH...HHHH.HIIII.DDDDDDDDDDD..DDDDDDDDDDD..EEEEEEEEEEE.ENNNN..NNNN..
# //.HHHH...HHHH.HIIII.DDDD...DDDD..DDDD...DDDD..EEEE........ENNNNN.NNNN..
# //.HHHH...HHHH.HIIII.DDDD....DDDD.DDDD....DDDD.EEEE........ENNNNN.NNNN..
# //.HHHHHHHHHHH.HIIII.DDDD....DDDD.DDDD....DDDD.EEEEEEEEEE..ENNNNNNNNNN..
# //.HHHHHHHHHHH.HIIII.DDDD....DDDD.DDDD....DDDD.EEEEEEEEEE..ENNNNNNNNNN..
# //.HHHHHHHHHHH.HIIII.DDDD....DDDD.DDDD....DDDD.EEEEEEEEEE..ENNNNNNNNNN..
# //.HHHH...HHHH.HIIII.DDDD....DDDD.DDDD....DDDD.EEEE........ENNNNNNNNNN..
# //.HHHH...HHHH.HIIII.DDDD...DDDDD.DDDD...DDDDD.EEEE........ENNN.NNNNNN..
# //.HHHH...HHHH.HIIII.DDDDDDDDDDD..DDDDDDDDDDD..EEEEEEEEEEE.ENNN..NNNNN..
# //.HHHH...HHHH.HIIII.DDDDDDDDDD...DDDDDDDDDD...EEEEEEEEEEE.ENNN..NNNNN..
# //.HHHH...HHHH.HIIII.DDDDDDDDD....DDDDDDDDD....EEEEEEEEEEE.ENNN...NNNN..
#                   An RP Text Based Adventure Game
# //.....................       By Matt      .............................



answer = input("Would you like to play a game? Yes/No : ")
if answer.lower().strip() == "yes":

    answer = input("You come to a junction, do you go left or right? left/right : ").lower().strip()
    if answer == "left":
        answer = input("You come across a gang of thugs, do you walk by them or go around them? (by/around) : ").lower().strip()

        if answer == "around":
            answer = input("You make the correct decision, you stumble acorss an old house, it's raining currently. Do you go inside for shelter? (Yes/No) : ").lower().strip()

            if answer == "yes":
                answer = input("After spending the night, you wake up refreshed, but your hungry, you go through the cupboards in the house and find an apple, do you eat it? (yes/no) : ").lower().strip()

                if answer == "no":
                    answer = input("You dodge a bullet there! lucky enough you see deer out of the window, after searching the house you find a hunting rifle with 3 rounds. You missed 2 shots do you risk a third on the deer? (yes/no) : ").lower().strip()


                    if answer == "yes":
                        answer = input("You hit the deer! as you already have a knife from the kitchen you start carving up the deer, do you spend another night at the house or move on? (stay/go) : ").lower().strip()

                        if answer == "stay":
                            answer = input("You spend one more night at the house, you wake up to find your no longer alone. its 3am and someone in downstairs, do you hide or head downstairs?  (hide/downstairs) : ").lower() .strip()                                                   
                

                            if answer == "hide":
                                answer = input("You make the right decision to hide, not knowing who is downstairs, you hear someone come up, they look around to find your backpack with all your essentials inside it, do you remain hidden or confront the person? (hidden/confront) : ").lower().strip()


                                if answer == "confront":
                                    answer = input("You put the guy to the floor taking back your backpack but also claiming a gun from the person, you make a run downstairs but are confronted by two others, do you shoot them? (yes/no) : ")

                                
                            
                                
                                # //.................................................................................................................................................
                                # //.MMMMMM...MMMMMM...OOOOOOO.....RRRRRRRRRR...EEEEEEEEEEE......TTTTTTTTTTO..OOOOOOO............CCCCCCC......OOOOOOO....MMMMMM...MMMMMMEEEEEEEEEEE..
                                # //.MMMMMM...MMMMMM..OOOOOOOOOO...RRRRRRRRRRR..EEEEEEEEEEE......TTTTTTTTTTO.OOOOOOOOOO.........CCCCCCCCC....OOOOOOOOOO..MMMMMM...MMMMMMEEEEEEEEEEE..
                                # //.MMMMMM...MMMMMM.OOOOOOOOOOOO..RRRRRRRRRRR..EEEEEEEEEEE......TTTTTTTTTTOOOOOOOOOOOOO.......CCCCCCCCCCC..OOOOOOOOOOOO.MMMMMM..MMMMMMMEEEEEEEEEEE..
                                # //.MMMMMMM.MMMMMMM.OOOOO..OOOOO..RRRR...RRRRR.EEEE................TTTT...OOOOO...OOOOO......CCCCC...CCCC.OOOOO...OOOOO.MMMMMMM.MMMMMMMEEEE.........
                                # //.MMMMMMM.MMMMMMMOOOOO....OOOOO.RRRR...RRRRR.EEEE................TTTT...OOOO.....OOOOO.....CCCC....CCC..OOOO.....OOOOOMMMMMMM.MMMMMMMEEEE.........
                                # //.MMMMMMM.MMMMMMMOOOO......OOOO.RRRRRRRRRRR..EEEEEEEEEE..........TTTT...OOOO......OOOO.....CCCC.........OOOO......OOOOMMMMMMM.MMMMMMMEEEEEEEEEEE..
                                # //.MMMMMMMMMMMMMMMOOOO......OOOO.RRRRRRRRRRR..EEEEEEEEEE..........TTTT...OOOO......OOOO.....CCCC.........OOOO......OOOOMMMMMMMMMMMMMMMEEEEEEEEEEE..
                                # //.MMMMMMMMMMMMMMMOOOO......OOOO.RRRRRRRR.....EEEEEEEEEE..........TTTT...OOOO......OOOO.....CCCC.........OOOO......OOOOMMMMMMMMMMMMMMMEEEEEEEEEEE..
                                # //.MMMMMMMMMMMMMMMOOOOO....OOOOO.RRRR.RRRR....EEEE................TTTT...OOOO.....OOOOO.....CCCC....CCC..OOOO.....OOOOOMMMMMMMMMM.MMMMEEEE.........
                                # //.MMMM.MMMMM.MMMM.OOOOO..OOOOO..RRRR..RRRR...EEEE................TTTT...OOOOOO..OOOOO......CCCCC...CCCCCOOOOOO..OOOOO.MMMMMMMMMM.MMMMEEEE.........
                                # //.MMMM.MMMMM.MMMM.OOOOOOOOOOOO..RRRR..RRRRR..EEEEEEEEEEE.........TTTT....OOOOOOOOOOOO.......CCCCCCCCCCC..OOOOOOOOOOOO.MMMM.MMMMM.MMMMEEEEEEEEEEE..
                                # //.MMMM.MMMMM.MMMM..OOOOOOOOOO...RRRR...RRRRR.EEEEEEEEEEE.........TTTT.....OOOOOOOOOO.........CCCCCCCCC....OOOOOOOOOO..MMMM.MMMMM.MMMMEEEEEEEEEEE..
                                # //.MMMM.MMMMM.MMMM....OOOOOO.....RRRR....RRRR.EEEEEEEEEEE.........TTTT......OOOOOOO............CCCCCCC......OOOOOOO....MMMM.MMMM..MMMMEEEEEEEEEEE..
                                # //.................................................................................................................................................



                                elif answer == "hidden":
                                    print("You should of confronted the person while you had the chance, they find you drag you downstairs and beat you to death.... Game Over")

                            elif answer == "downstairs":
                                print("You made a bad move, there is more than one downstairs, they beat you to death and toss your body outside..... Game Over")


                        elif answer =="go":
                            print("You leave the house to discover there was a gang watching you the whole time, they catch you and beat you to death..... Game Over!")

                    elif answer == "no":
                        print("You should of taken the shot! ..... Game Over") 

                elif answer == "yes":
                    print("After taking a bite out of the apple, you discover it's covered in posion! ...... Game Over")


            elif answer == "no":
                print("You wonder helplessly into the darkness, trip up breaking your leg unable to move and noone around to help you. Game Over")

        elif answer == "by":
            print("Oh no you made the wrong decision, they beat you up and throw you into the river...... Game over")


    elif answer == "right":
        print("You went down the wrong road try again!   Game Over")

    else:
        print("Invalid choice, you lost!")

else:
    print("That's to bad!")
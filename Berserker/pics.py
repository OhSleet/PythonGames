
print("       ,      , ")
print("      /(.-""-.)\ ")
print("  |\  \/      \/  /|")
print("  | \ / =.  .= \ / |")
print("  \( \   o\/o   / )/")
print("   \_, '-/  \-' ,_/")
print("     /   \__/   \ ")
print("     \ \__/\__/ /")
print("   ___\ \|--|/ /___")
print(" /`    \      /    `\ ")
print("|      '----'        | ") 


print("            {)      ")
print("         c==//\     ")
print("    _-~~/-._|_|      ")
print("   /'_,/,   //'~~~\;;,   ")
print("   `~  _( _||_..\ | ';;  ")
print("     /'~|/ ~' `\<\>  ;   ")
print("    /  |      /  |  ")


print("                                                                                                          ,^.                   ")
print("                                                                                                          |||                    ") 
print("                                                                                                          |||       _T_           ")
print("                                                                                                          |||   .-.[:|:].-.       ")
print("                                                                                                          ===_ /\|   '   |/       ")   
print("                                                                                                          E]_|\/ \--|-|''''|      ")
print("                                                                                                         O  `'  '=[:]| A  |      ")
print("                                                                                                                /####|  P |       ")
print("                                                                                                               /#####`.__.'       ")
print("                                                                                                               / \/###\/\       ")
print("                                                                                                               | \     / |       ")
print("                                                                                                               | |     | |       ")
print("                                                                                                            <####)     (####>      ")




import os
import time

def animate_Rocket():
  distanceFromTop = 20
  while True:
    print("\n" * distanceFromTop)
    print("          /\        ")
    print("          ||        ")
    print("          ||        ")
    print("         /||\        ")
    time.sleep(0.2)
    os.system('clear')  
    distanceFromTop -= 1
    if distanceFromTop <0:
      distanceFromTop = 20
  
  
#Main Program Starts Here....
animate_Rocket()


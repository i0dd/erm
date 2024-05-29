print("hi welcome to the game \n \n \n ")

print("press 1 -  would like to go on adventure i  the forest!!!!! \npress 2 - would like to sleep all day")


firstchoice = input(": ")

if firstchoice == "1":
    print(" WOO U GOIGN ON ADVENTURE!!!! \n + 5 enjoyment \n \n ")

    print("u felt hungury \npress 1 to go find a tree to find food \npress 2 to keep going on the adventure")

    wji = input(": ")
    if wji == "1":
      print("u tried finding tree but u died")

    elif wji =="2":
       print("u found a monster")
       print("press 1 to run away \npress 2 to fight ")

       ji = input(": ")
       if ji == "1":
          print(" u tried runing but  the monster killled u")

       elif ji == "2":
          print("u tried fighting back but died")

       else:
          print("kys")

    else:
       print("kys")

elif firstchoice == "2":
   print(" neg 10")

else:
   print("kys")



print("end game \nBYE")
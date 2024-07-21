# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    print("keep moving")

    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


    #  Task 2: Setting the Scene

    place = input("Choose a place: forest or cave? ")

if place == "forest":
    print("keep moving")

    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("do you want to light a torch ?") 
else:
     print("proceed in the dark")

#  Task 3: Default Path
place = input("Choose a place: forest or cave? ")
if place == "forest":
    print("keep moving")

    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("do you want to light a torch ?") 

place =input("chose a place: desert or attic")
if place == "neither desert or attic":
     pass
elif  place == "desrt":
    print("take a pack of water ")

elif place == "attic":
    print("take warm cloths")
else:
    print("do not go")


    ## 2. Quick Decisions: The Event Planner 🎉

attendees = input("Enter number of attendees: ")

if attendees > 100:
    print("large hall")

elif attendees < 100:
    print("connference room")

# Catering Choices

food_choice = input("choose a choice of food: vegetarian or Gourment meals")
if food_choice ==("vegetarian"):
    print("i recommend Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")
    
print("Welcome to my first game!")
print("To get started right away, I need to know who's playing.")
name = input("What is your name? ")
age = input("Thanks, how old are you? ")

if int(age) <= 8:
    print("Hi", name, ", you can play but might need an adult to supervise.")
else:
    print("Hi", name, ", you are old enough to play")
print()
wants_to_play = input("Shall we start? (Y/N) ").lower()
if wants_to_play == "y":
    print("Let's play!")
    print(
        "You are walking through the woods and you struck by the smell of food making you hungry. You try to follow the scent and stumble upon an open house. Inside the house you see three bowls of porridge on the table."
    )
    bowls = input("Which bowl do you try first (1/2/3) ")
    if int(bowls) == 1:
        print(
            "Agh! It's too hot and you have burnt your tongue. Go for  a walk and play again to let it cool down when you come back."
        )
    elif int(bowls) == 2:
        print(
            "Eww! It's cold and gloopy. Put it in the microwave and play again to warm it up."
        )
    elif int(bowls) == 3:
        print(
            "Yummy! This bowl is just right. You need to sit down to enjoy this. Let's go to the living room to enjoy. In the living room you see three chairs of various sizes.")
        chairs = input("Which chair do you sit in first? (1/2/3)? ")
        if int(chairs) == 1:
              print("This chair is too big and you can't get to play the rest of the game.")
        elif int(chairs) == 2:
              print("This chair is too small and now you are stuck. Sorry you unable to continue the game.")
        elif int(chairs) == 3:
              print("Oh, this chair is just right and so comfy but you cannot put your feet up to nap. Go to the bedroom, there might be a bed waiting for you.")
              beds = input("The bedrooms are upstairs and again you note three beds to sleep in. Which bed should you try? (1/2/3) ")
              if int(beds) == 1:
                    print("Uh-oh, this bed is far too lumpy and has no pillow. Frustrated, you storm out of the house and make your way home.")
              elif int(beds) == 2:
                    print("It's comfy bed, too comfy infact that you sleep but lose track of time. It's too dark to go home and you can hear three bears downstairs...")
              elif int(beds) == 3:
                    print("It's perfect and gives you the most restful sleep you have had in a long time. You wake up and make your way home. Along the path you pass three bears commenting on their porridge. Phew! Thank goodness you never got caught in their house. Thank you for playing.")
              else:
                    print("Wrong entry! Try again!")
        else:
              print("Wrong entry! Try again!")
    else:
          print("Wrong entry! Try again!")
else:
    print("That's fine come back later.")

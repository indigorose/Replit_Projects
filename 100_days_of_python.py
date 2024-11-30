# Day 1

# 1. Create a greeting for your program.
print("Hey! Heard your looking for a new band name, let me help.")
# 2. Ask the user for the city that they grew up in.
city_first = input("What city did you grow up in?\n")
# 3. Ask the user for the name of their pet.
pet_second = input("Thanks, what about the name of your pet? \n")
# 4. Combine the name of their city and pet and show them their band name.
print("Got it! I think your new band name should be " +
      city_first + " " + pet_second + ". Sounds pretty cool huh?")

#  Day 2

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

print((int(two_digit_number[-2])+(int(two_digit_number[-1]))))


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round((float(weight))/((float(height)) ** 2))

print(bmi)

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age_as_int = int(age)
years_left = 90 - age_as_int
days_left = years_left*365
weeks_left = years_left*52
months_left = years_left*12


message = (f"You have {days_left} days, {
           weeks_left} weeks, and {months_left} months left")

print(message)

# Day 3
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if (height >= 120):
    print("Can ride")
else:
    print("Can't ride")

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

choice_1 = input("Left or Right? ")
if choice_1.lower() == "left":
    choice_2 = input("Swim or Wait? ")
    if choice_2.lower() == "wait":
        choice_3 = input("Which Door? ")
        if choice_3.lower() == "red":
            print("Burned by fire. \n Game Over.")
        elif choice_3.lower() == "blue":
            print("Eaten by beasts.\n Game Over")
        elif choice_1.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked byt trout. \n Game Over.")
else:
    print("Fall into a hole. \n Game Over.")

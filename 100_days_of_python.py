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

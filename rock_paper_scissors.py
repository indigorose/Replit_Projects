import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

pc = int(input("What do you choose? Type 0 for Rock, 1 for Paper  or 2 for Scissors\n"))

if int(pc == 0):
    print(rock)
elif int(pc) == 1:
    print(paper)
elif int(pc) == 2:
    print(scissors)
else:
    print("NaN")

print("Computer chose: ")

cc = int(random.randint(0, 2))

if int(cc) == 0:
    print(rock)
elif int(cc) == 1:
    print(paper)
elif int(cc) == 2:
    print(scissors)
else:
    print("NaN")

if (pc == 0 and cc == 2) or (pc == 1 and cc == 0) or (pc == 2 and cc == 1):
    print("You won")
elif (pc == 1 and cc == 2) or (pc == 0 and cc == 1) or (pc == 2 and cc == 0):
    print("You lost")
elif pc == cc:
    print("Its a tie!")
else:
    print("Not working")

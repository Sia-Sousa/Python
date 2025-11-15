import random

player = 0
computer = 0

print (" 1) ✊\n 2) ✋\n 3) ✌️\n")
player = int(input("Pick a number: "))

computer = random.randint(1,3)

computer

if player == 1 and computer == 3:
    print("You chose: ✊ \nCPU chose: ✌️ \nThe player won! ")
elif player == 3 and computer == 1:
    print("You chose: ✌️ \nCPU chose: ✊ \nThe CPU won! ")
elif player == 3 and computer == 2:
    print("You chose: ✌️ \nCPU chose: ✋ \nThe player won! ")
elif player == 2 and computer == 3:
    print("You chose: ✋ \nCPU chose: ✌️ \nThe CPU won! ")
elif player == 1 and computer == 2:
    print("You chose: ✊ \nCPU chose: ✋ \nThe CPU won! ")
elif player == 2 and computer == 1:
    print("You chose: ✋️ \nCPU chose: ✊ \nThe player won! ")
else:
    print ("Invalid.")
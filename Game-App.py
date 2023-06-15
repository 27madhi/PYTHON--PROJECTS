"GAME APPLICATION"



import random

user_win=0
computer_win=0
options=["rock","paper", "scissor"]
while True:
    user = input ("type rock\paper\scissor or q to quit: ").lower()

    if user == "q":
        break
    if user not in options:
        continue
    random_num= random.randint(0,2)
    computer = options[random_num]
    if user =="rock" and computer =="scissor":
        print ("you won!")
        user_win+=1
    elif user =="paper" and computer == "rock":
        print ("you won!")
        user_win+=1
    elif user == "scissor" and computer == "paper":
        print("you won!")
        user_win+=1
    else:
        print ("you loss")
        computer_win+=1
print("user wins a",str(user_win),"times")
print ("computer wins","a", str(computer_win),"times")
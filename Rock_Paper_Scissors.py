import random

print("welcome to rock,paper and scissors")
print("select 1 for rock \nselect 2 for paper \nselect 3 for scissors")

winningpts = int(input("select points required to win"))

cmppts = 0
userpts = 0

# 1 = rock
# 2 = paper
# 3 = scissors

while True:

    userchoice = int(input("enter your choice"))
    compchoice = random.randint(1, 3)
    if userchoice not in [1, 2, 3]:
        print("Invaild choice")
        continue

    if (userchoice == compchoice):
        print("draw")

    elif (userchoice == 1 and compchoice == 2):
        print("you lose")
        cmppts = cmppts + 1

    elif (userchoice == 1 and compchoice == 3):
        print("you win")
        userpts = userpts + 1

    elif (userchoice == 2 and compchoice == 1):
        print("you win")
        userpts = userpts + 1

    elif (userchoice == 2 and compchoice == 3):
        print("you lose")
        cmppts = cmppts + 1

    elif (userchoice == 3 and compchoice == 1):
        print("you lose")
        cmppts = cmppts + 1

    elif (userchoice == 3 and compchoice == 2):
        print("you win")
        userpts = userpts + 1

    user = ""

    if (userchoice == 1):
        user = "rock"

    elif (userchoice == 2):
        user = "paper"

    elif (userchoice == 3):
        user = "scissors"

    bot = ""

    if (compchoice == 1):
        bot = "rock"

    elif (compchoice == 2):
        bot = "paper"

    elif (compchoice == 3):
        bot = "scissors"
    print("You chose", user)
    print("bot chose", bot)

    print("Computer points= ", cmppts)
    print("User points= ", userpts)

    if (userpts == winningpts or cmppts == winningpts):
        break

if (userpts > cmppts):
    print("You won the match")

elif (userpts < cmppts):
    print("You lost the match")
print("Computer points= ", cmppts)
print("User points= ", userpts)
import random
level=input("Enter easy or hard :")
num=random.randint(0,100)

def game(choice):
    if num < choice:
        print("Too high!")
    elif num > choice:
        print("Too Low!")
    else:
        return 1

def attempt(chance):
    for n in range(chance):
        print(f"______Attempt left={chance-n}")
        choice = int(input("Enter number :"))
        play=game(choice)
        if play==1:
            print("You won")
            break

if level=="easy":
    attempt(10)
elif level=="hard":
    attempt(5)
import random
from blackjack import art
print(art)
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def rand():
    return random.choice(card)

num_your=0
num_comp=0
num_your+=rand()
num_comp+=rand()
chs=True
while chs:
    num_your+=random.choice(card)
    print(f"You score {num_your}\ncomputer score {num_comp}")
    if num_your<21:
        check = input("Press y to continue and n to stop :")
    if check =="n" or num_your>=21:
        chs=False

if num_your>21 :
    print(f"\nYour score :{num_your}\nComputer Score :{num_comp}\nYou Loose")

while num_comp<17:
    num_comp += random.choice(card)

if num_comp>num_your and num_comp<=21:
    print(f"\nYour score :{num_your}\nComputer Score :{num_comp}\nYou Loose")
elif num_your==num_comp:
    print("\nDraw")
elif (num_your>num_comp and num_your<=21) or num_comp>21:
    print(f"\nYour score :{num_your}\nAnd Computer score {num_comp}")
    print("You won")

import random

chs=int(input("Choose\n0.Rock\n1.Paper\n2.Scissior\n>>"))
gen=random.randint(0,2)

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissior=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print(gen)
if gen==0:
    print(f"computer choose\n{rock}")
    print("You choose\n")
    if chs==0:
        print(rock)
        print("Draw!")
    elif chs==1:
        print(paper)
        print("You Loose!")
    elif chs==2:
        print(scissior)
        print("You Won!")
elif gen==1:
    print(f"computer choose\n{paper}")
    print("You choose\n")
    if chs==0:
        print(rock)
        print("You Won!")
    elif chs==1:
        print(paper)
        print("Draw!")
    elif chs==2:
        print(scissior)
        print("You Loose!")

elif gen==2:
    print(f"computer choose\n{scissior}")
    print("You choose\n")
    if chs==0:
        print(rock)
        print("You Loose!")
    elif chs==1:
        print(paper)
        print("You Won!")
    elif chs==2:
        print(scissior)
        print("Draw!")


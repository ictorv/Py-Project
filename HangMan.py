
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      ''')
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word=['s','o','l','v','e']
emp=['_','_','_','_','_']
life=7
chg = 0
while life>1:
    print(emp)
    if chg==0:
        life-=1
        print(HANGMANPICS[7-life])
    lett = input("Enter alphabet:")
    chg=0
    for pos in range(0,5):
        if word[pos]==lett:
            emp[pos]=lett
            chg=1
    if word == emp:
        break

if word!=emp:
    print("You loose!")
else:
    print("You Won!")
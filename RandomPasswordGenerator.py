import random

let=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','<','>','/','?',';',',','.']

con1=int(input("How many letter do you want?"))
con2=int(input("How many integer do you want?"))
con3=int(input("How many symbol do you want?"))

pwd=''
for a in range(0,con1):
    # gen=random.randint(0,len(let)-1)
    # pwd=pwd+let[gen]
    pwd+=random.choice(let)

for a in range(0,con2):
    # gen=random.randint(0,len(num)-1)
    # pwd=pwd+num[gen]
    pwd += random.choice(num)

for a in range(0,con3):
    # gen=random.randint(0,len(sym)-1)
    # pwd=pwd+sym[gen]
    pwd += random.choice(sym)

new_pwd=''.join(random.sample(pwd,len(pwd)))
print(new_pwd)

# OR
# pwd=[]
# for a in range(0,con1):
#     pwd.append(random.choice(let))
#
#
# for a in range(0,con2):
#     pwd += random.choice(num)
#
# for a in range(0,con3):
#     pwd += random.choice(sym)
#
# random.shuffle(pwd)
#
# # converting list into string
# pw=""
# for ch in pwd:
#     pw+=ch
# print(pw)

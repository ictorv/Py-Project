from art import logo
print(logo)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # alphabet position
    # def pos(lett, alp):
    #     i=0
    #     while alp[i]!=lett:
    #         i+=1
    #     print (i+1)

    # def encrypt(text, shift):
    #     new_txt=""
    #     for n in text:
    #         posi=alphabet.index(n)
    #         new_txt+=alphabet[posi+shift]
    #     print(new_txt)
    #
    # def decrypt(text, shift):
    #     new_txt=""
    #     for n in text:
    #         posi=alphabet.index(n)
    #         new_txt+=alphabet[posi-shift]
    #     print(new_txt)

def ceaser(text, shift, direction):
    new_txt=""

    for n in text:
        if n in alphabet:
            posi=alphabet.index(n)
            if direction=="encrypt":
                new_txt+=alphabet[posi+shift]
            elif direction=="decrypt":
                new_txt += alphabet[posi-shift]
        else:
            new_txt+=n
    print(new_txt)

wanna_continue=True

while wanna_continue:
    direction=input("Enter encrypt or decrypt :")
    text=input("Enter Text :").lower()
    shift=int(input("Enter shift number :"))
    shift=shift%25
    ceaser(text, shift, direction)
    # if direction=="encrypt":
    #     encrypt(text,shift)
    # elif direction=="decrypt":
    #     decrypt(text,shift)
    res=input("Want to continue? Enter yes or no :")
    if res=="no":
        wanna_continue==False
        print("Good Bye!")


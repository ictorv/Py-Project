a=int(input("Enter upper range :"))
b=int(input("Enter lower range :"))
for num in range(a,b+1):

    if num%3==0 and num%5==0:
        print("FizzBuzz!")
    elif num % 3==0:
        print("Fizz!")
    elif num % 5==0:
        print("Buzz!")
    else:
        print(num)
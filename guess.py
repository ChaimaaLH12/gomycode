import random
print("Welcome to the Guess the Number game! \n I'm thinking of a number between 1 and 100. Can you guess what it is?")
x = int(random.randint(1,100))
print(x)
n = int(input("Enter your guess:"))
while n != x :
    if n > x :
        print("Your guess is too high. Guess again. ")
        n = int(input("Enter your guess:"))
    elif n < x : 
        print(" Your guess is too low . Guess again. ")
        n = int(input("Enter your guess:"))
    if n == x:
       print("Congratulations! You guessed the number correctly!")
       break

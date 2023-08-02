#begin by defining hidden number
import random 
n = random.randrange(1,10)
#number is already defined here but not printed. It is a random number
#in the range of 1-10
guess = int(input("Enter any number: "))
#this sets the value of guess equal to the integer value of the user's input
#This makes sure that the value entered by the user gets changed to 
#an integer rather than a word
#It also gives the input a place to live, which is after Enter any number:
while n!= guess:
#this is a conditional that says while n is not equal to guess
#after this conditional, the code gets indented and you specify
#the actions taken according to the input. Exclamation mark means 
#not this
    if guess < n:
        print("too low")
        guess = int(input("Enter numnber again: "))
#If the guess is smaller than the number, the code will display "too low" 
#It will also display a new message for the input to live "Enter number again"
    elif guess > n:
        print ("Too high!")
        guess = int(input("Enter number again: "))
#If the guess is larger than the number, the code "too high" will be displayed
#New message for the input to live "Ener number again: "
    else:
        break
print("you guessed it right!")
#If their guess was not greater or lesser than the number, then they were right!
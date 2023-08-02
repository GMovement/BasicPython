#This is a dice rolling game, where we need to have random values generated
#from 1 to 6 for each of the 2 dice. We then print those values to the 
#screen.
#we start by importing the random module, which allows for random number
#generation as well as for a range for those random numbers. Max and min
#values are the highest and lowest number that can be randomly generated
import random
min_value=1
max_value=6
#We also want to program this game to run again and again
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are...")
    #these next 3 lines generate the values and print them both onscreen. 
    #the way it does this is by using the random module to select a 
    #random integer from the range set at the beginning of the minimum
    #value and the maximum value. It then prints the result to the screen
    value1=random.randint(min_value, max_value)
    value2=random.randint(min_value, max_value)
    print(value1,value2)
    roll_again = input("Press 'y' or 'yes' to roll the dice again: ")
print("Have a good day")
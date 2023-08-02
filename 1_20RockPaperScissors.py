from random import randint
#imports randint from random module, allows for a random number to be chosen
t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]
#we set t equal to the list of Rock, Paper, Scissors. Each of these are 
#it's own seperate value, so when we use randint, it randomly selects the 
#value 0, 1 or 2. That's the values of Rock, Paper or Scissors respectively
#it then sets one of those values as the value of computer. So computer
#equals Rock or Paper or Scissors, randomly

player = False
#player is set to be equal to false because the player value is determined by the 
#user input. Only when an input has been entered can this program run. Basically
#False is the off switch, and the input turns it on.

while player == False:
    player = input("Rock, Paper, Scissors? \n")
    #this prints to the screen and prompts the user to input one
    if player == computer:
        print("Tie!")
    #In case the value for both the random generated computer and the user
    #input are the same, it will print Tie!
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling")

import random
#reference both lists contained in the same directory 
#and then make them both lists

with open("adjectives.txt") as f:
     description = f.read().splitlines()

with open("nouns.txt") as g:
    drink = g.read().splitlines()

first = random.choice(description)
second = random.choice(drink)

while True:
    user_input = input('Do you want to create a new drink name? Yes/No: ')
    if user_input.lower() == "yes":
        print(first + " " + second)
        break

    elif user_input.lower() == "no":
        print("Too bad!" + first + " " + second)
        break

    else: print("I don't understand that")
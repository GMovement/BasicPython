#for hangman, there are a number of different things we need to play
#this game. The first is the random module. 
import random
from words import word_list
#the random module has a word list in it. We can create a function that will 
#generate a random word from the word list. We also specify that when the 
#word is generated, it comes back in all caps so it's uniform.

def get_word():
    word = random.choice(word_list)
    return word.upper()
#We now need to define another function. This function will show the dash
#symbol - in place of the letters of the word. So the word cat would be
#_ _ _ or the word letter would be _ _ _ _ _ _ This shows how many letters 
#make up the word. It also defines the value of guessed as being equal to 
#False

def play(word):
    word_completion = "_ " = len(word)
    guessed = False
#We then create two lists, one to hold the letters the user guessed, and the 
#other to hold the words the user guessed
    guessed_letters = []
    guessed_words = []
#We then define the variable of tries. This counts the 4 limbs, body and head
#that all disappear with every wrong guess
    tries = 6
#We then print a greeting, the length of the word in the form of dashes, and
#\n which means printing a new line
    print("Let's play hangman!")
    print(word_completion)
    print("\n")
#
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():


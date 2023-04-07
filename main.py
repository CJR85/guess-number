#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
# Choosing a random number between 1 & 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

# Make function to set difficulty

# Let user guess a number

# Function to check user's guess against actual answer

# Track the number of turns remaining & reduce by 1 is they get it wrong

# Repeat the guessing if they get it wrong
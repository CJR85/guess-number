#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer is {answer}.")


# Make function to set difficulty
def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
  # Choosing a random number between 1 & 100
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"The correct answer is {answer}.")

  turns = set_difficulty()
  print(f"You have {turns} attempts remaining to guess the number.")

  # Repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    # Let user guess a number
    guess = int(input("Make a guess: "))
    check_answer(guess, answer)


# Track the number of turns remaining & reduce by 1 is they get it wrong

game()
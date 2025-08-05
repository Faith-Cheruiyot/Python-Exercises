# Question Two
# Write a guessing game where the user has to guess a number between 1 and 10 inclusive.
import random
correct_guess = random.randint(1, 10)
tries = 0
max_tries = 5

while tries < max_tries:
    guess = int(input("Guess a number between 1 and 10: "))

    if 1 <= guess <=10:
        print(f"You guessed: {guess}")
        if guess == correct_guess:
            print("Congratulations! You guessed the correct number.")
            break
        difference = abs(correct_guess - guess)
        if difference > 5:
            print("Not even close!")
        elif difference <= 5 and difference >= 2:
            print("Close!")
        elif difference < 2:
            print("Almost there!")
    else:
        print("Invalid guess. Please enter a number between 1 and 10.")
    tries += 1
if tries == max_tries:
    print(f"Sorry, you've used all your tries. The correct number was {correct_guess}.")          



    
    

    


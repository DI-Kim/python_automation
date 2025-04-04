# This is a guess the number game.
import random

print('Hello, What is your name?')
username = input()
secret_number = random.randint(1, 20)
print(f'Well, {username}, I am thinking of a number between 1 and 20.')

# debug code
# print(f'Secret number is {secret_number}')

for guess_taken in range(6):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess.

if guess == secret_number:
    print(
        f'Good job, {username}! You guessed my number in {guess_taken + 1} guesses!')
else:
    print(
        f'Sorry, {username}. The number I was thinking of was {secret_number}.')

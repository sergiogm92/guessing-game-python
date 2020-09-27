import random

print("----------------------------")
print("     M&M guessing game!")
print("----------------------------")

print('Guess the number of M&Ms and you get lunch on the house')
print()

mm_count = random.randint(1, 100)
attempt_limit = 5
attemps = 0

while attemps < attempt_limit:
    guess_text = input('How manu M&Ms are in the jar? ')
    guess = int(guess_text)
    attemps += 1

    if mm_count == guess:
        print(f'You got a free lunch! It was {guess}.')
        break
    elif guess < mm_count:
        print("Sorry, that's too low!")
    else:
        print("That's too high")

print(f"Bye, you're done in {attemps}")

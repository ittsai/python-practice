from art import guess_logo
import random

print(guess_logo)
print("\n")
print("Guess a number from 1 to 100")

correct_number = random.randint(1, 100)
number_from = 1
number_to = 100
your_number = int(input("Give a number: "))

while correct_number != your_number:
    if correct_number > your_number:
        number_from = your_number
        print(f"Higher, number between {number_from} to {number_to}")
        your_number = int(input("Give a number: "))
    else:
        number_to = your_number
        print(f"Lower, number between {number_from} to {number_to}")
        your_number = int(input("Give a number: "))

print(f"Correct! The number is {correct_number}")
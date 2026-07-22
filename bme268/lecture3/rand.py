number = 48

print("I have a number between 1 and 100. Can you guess it?")

while True:

        guess = int(input("Your Guess?: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! ")
            break

print("Game over")
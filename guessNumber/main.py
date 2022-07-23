import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} "))
        if (guess > random_number):
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
    print(f"You've guessed the number {random_number} correctly!")
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = high

        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        print(low,high)
    print(f"I've guessed the number {guess} correctly")



computer_guess(10)

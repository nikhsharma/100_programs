from random import randint

def guess_number():
    num = randint(0, 101)
    guess = ""
    while guess != num:
        guess = input('Guess a number between 0-100:   ')
        if guess < num: print("Guess Higher!")
        if guess > num: print("Guess Lower!")
        if guess == num: print("Correct!")

end = False
while end == False:
    fin = raw_input("Press 'Y' to play. Press 'X' to exit:    ").upper()
    if fin == "Y":
        guess_number()
    if fin == "X": end = True

import random
playing = True
number = str(random.randint(10,20))
print("i will generate a number from 0 to 9, and you hace to guess the number 1 digit at a time.")
while playing:
    guess = input("Give e your best guess!")
    if number == guess:
        print("congratulations! you guessed the number")
        break
    else:
        print("sorry, wrong guess. try again!")
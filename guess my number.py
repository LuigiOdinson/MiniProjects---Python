number = 7
lives = 3+1
win = True
print("Guess my number: ", end='')
guess_number = int(input())
while guess_number != number:
    lives -= 1
    if lives == 0:
        win = False
        break
    print("Wrong, you have " + str(lives) + " lives left")
    print("Try again: ", end='')
    guess_number = int(input())
if win:
    print("you won")
else:
    print("you lost")



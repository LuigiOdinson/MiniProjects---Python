import random
options = [1, 2, 3]
a_points = 0
b_points = 0
rounds = 3
switcher = {
    1: "Scissors",
    2: "Paper",
    3: "Rock",
}
def checkwin(a_opt, b_opt):
    win = 0
    if a_opt == 1 and b_opt != 1:
        if b_opt == 2:
            win = 1
        elif b_opt == 3:
            win = 2
    elif a_opt == 2 and b_opt != 2:
        if b_opt == 1:
            win = 2
        elif b_opt == 3:
            win = 1
    elif a_opt == 3 and b_opt != 3:
        if b_opt == 1:
            win = 1
        elif b_opt == 2:
            win = 2
    else:
        win = 0
    return win

while rounds > 0:
    print("YOU'RE PLAYER A\n1)Scissors 2)Paper 3)Rock")
    print("Choose your move: ", end='')
    a_opt = int(input())
    b_opt = random.choice(options)
    win_num = checkwin(a_opt, b_opt)
    if win_num == 1:
        a_points += 1
    elif win_num == 2:
        b_points += 1
    print("A:" + switcher.get(a_opt) + " B:" + switcher.get(b_opt))
    print("POINTS: A:" + str(a_points) + " B:" + str(b_points) + "\n")
    rounds -= 1

if a_points > b_points:
    print("A has won the game")
elif a_points < b_points:
    print("B has won the game")
else:
    print("The game was tie")

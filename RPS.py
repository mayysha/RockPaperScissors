import random


def is_win(player, opponent):
    if (player == "Rock" and opponent == "Scissors") or (player == "Scissors" and opponent == "Paper") or (player =="Paper" and opponent == "Rock") :
        return True

def play():

    user = input("Type 'Rock','Paper' or 'Scissors'!")
    computer = random.choice(['Rock', 'Paper', 'Scissors'])
    print(computer)


    if user != computer :
        if is_win(user,computer):
            print("You Won!")

        else:
            print("You Lost")

    else:
        print("It's a tie!")


if __name__ == "__main__":
    play()
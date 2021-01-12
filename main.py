import random



def game(choice):
    ''' Creates Rock Paper Scissors Game.'''

    gameOptions = ['ROCK', 'PAPER', 'SCISSORS']

    rndChoice = random.randint(0,2)
    computer = gameOptions[rndChoice]

    player = False

    while player == False:
        player = choice
        player = player.upper()

        if player == "SCISSOR":
            player = "SCISSORS"

        if player == computer:
            print("TIE!")
            print("Computer chose: " + computer)
        elif (player == "ROCK") and (computer == "SCISSORS"):
            print("YOU WIN!")
            print("Computer chose: " + computer)
        elif (player == "PAPER") and (computer == "ROCK"):
            print("YOU WIN!")
            print("Computer chose: " + computer)
        elif (player == "SCISSORS") and (computer == "PAPER"):
            print("YOU WIN!")
            print("Computer chose: " + computer)
        else:
            print("YOU LOST!")
            print("Computer chose: " + computer)

if __name__ == '__main__':
    choice = raw_input("Choose Rock, Paper or Scissors: ")
    game(choice)


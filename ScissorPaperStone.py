#Implementation of a Scissor Paper Stone game

endGame = "False"
while endGame == "False":

    print('Player 1 turn, choose rock(1) paper(2) scissors(3)')

    player1 = "scissors"
    print('Player 2 turn, choose rock(1) paper(2) scissors(3)')

    player2 = "paper"

    #Check user input


    #Check winning condition
    if (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "scissors"):
        print('player 1 wins')
    else:
        print('player 2 wins')

    #Ask player for next game
    endGame = input()

    print("Next Game" , endGame)
    if endGame == "True":
        print('game ends')
        break
    else:
        continue
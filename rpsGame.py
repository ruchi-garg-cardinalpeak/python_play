#This is a Rock Paper Scissor game.
import random, sys

print('ROCK, PAPER, SCISSOR')

#These variables keep track of the wins, loses and ties
wins = 0
losses = 0
ties = 0

while True: #The main game loop.
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit the program
        if playerMove=='r' or playerMove == 'p' or playerMove == 's':
            break #Break out of the player input loop.
        print('Type one of thee: r, p, s, or q')
        
    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK verses ...')
    elif playerMove == 'p':
        print('PAPER verses ...')
    elif playerMove == 's':
        print('SCISSORS verses ...')
    
    # Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove ='r'    
        print('ROCK')
    elif randomNumber == 2:
        computerMove ='p'    
        print('PAPER')
    elif playerMove == 3:
        computerMove ='s'
        print('SCISSORS')
        

    # Display and record the win/loss/tie:
    if playerMove == computerMove: 
        print('It is a tie!')
        ties = ties + 1
        
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

if guess == secretNumber:
    print('Good Job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    ('Nope. The number I was thinking of was ' + str(secretNumber))

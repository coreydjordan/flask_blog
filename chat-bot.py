import random

def coin_game():
    #I put the whole loop in a function so I could use the play again functionality
    keep_looping = True
    #setting the inital while to true
    streak = 0
    #starting streak at 0
    winning = 3
    runner_up = 2
    #setting the grand prize streak at 3
    while keep_looping:
        guess = int(input('pick 1 for heads and 2 for tails '))
        #getting user input as an integer 
        coin_toss = 1
        #making coin_toss (the computer opponent) choose a random number between 1 and 2
        if guess == coin_toss:
            #if guess and coin toss are the same...
            streak += 1
            #streak goes up 1. (streak += 1 is the same as streak = streak + 1, this just saves you time)
            print(f'you win, your streak is {streak}!')
            #f statement saying you win and what the streak is now, the loop will go again
        else:
            again = input(f'you chose {guess} and the comp chose {coin_toss}, so you lose! Want to play again? y/n? ')
            #the only other condition is is the coin_toss and guess are different, then ask the user if they want to play again
            if again == 'y':
                #if again is equal to y, run the function again
                coin_game()
                #re running the entire function
            else:
                print('okay, thanks for playing!') 
                keep_looping = False
                #if they chose n, print statement, and stop the loop
        if coin_toss != guess and streak == runner_up:
            print('you were so close, you win $250!')
        elif streak == winning:
            print('You win $500!')
            #if their streak gets to 3, stop the loop and tell them they win
            keep_looping = False
            
            
coin_game()
# calling the function





import random
print('Welcome to Hand Cricket Simulator')
print('This game will be using 0-6 numbers only.')
print('The toss will now start')
# code for toss and pick
toss = input('Heads or Tails: ')
a = random.randrange(1, 3, 1)
if a == 1 and toss.lower() == 'heads':
    print(f'The coin has flipped to show {toss.upper()}! You won the toss!')
    pick = input('Do you want to bat or bowl? \n')
    print(f'You have chosen to {pick.upper()}')
elif a == 1 and toss.lower() != 'heads':
    print(f'The coin has flipped to show HEADS. You lost the toss.')
    pick_number = random.randrange(1, 3, 1)
    if pick_number == 1:
        pick = 'bat'
    else:
        pick = 'bowl'
    print(f'You have to {pick.upper()}')
elif a == 2:
    if toss.lower() == 'tails':
        print(f'The coin has flipped to show {toss.upper()}! You won the toss!')
        pick = input('Do you want to bat or bowl? \n')
        print(f'You have chosen to {pick.upper()}')
    else:
        print(f'The coin has flipped to show TAILS. You lost the toss.')
        pick_number = random.randrange(1, 3, 1)
        if pick_number == 1:
            pick = 'bat'
        else:
            pick = 'bowl'
        print(f'You have to {pick.upper()}')
# code for gameplay
if pick.lower() == 'bat':
    bat_status = 0
    print('You will now start batting.You will be out if you input number more than 6.')
    first_batting_total = 0
    while bat_status == 0:
        batting = int(input('Input a number between 0 and 6: '))
        bowling = random.randrange(7)
        print(f'Computer bowled a {bowling}')
        if batting > 6:
            bat_status = 1
        elif batting != bowling:
            bat_status = 0
            first_batting_total = first_batting_total + batting
        elif batting == bowling:
            bat_status = 1
            print('YOU ARE OUT!')
            print(f'You have set a target of {first_batting_total}')
        print(f'Your score is {first_batting_total}')
    print('You will now start bowling')
    second_batting_total = 0
    bowl_status = 0
    while bowl_status == 0:
        bowling = int(input('Input a number between 0 and 6: '))
        batting = random.randrange(7)
        print(f'Computer hit {batting} runs')
        if bowling != batting:
            bowl_status = 0
            second_batting_total = second_batting_total + batting
            print(f'Computer score is: {second_batting_total}')
        if second_batting_total > first_batting_total:
            bowl_status = 1
            winner = 1
        elif batting == bowling:
            bowl_status = 1
            print('Computer is OUT!')
            winner = 0
elif pick.lower() == 'bowl':
    bowl_status = 0
    first_batting_total = 0
    while bowl_status == 0:
        bowling = int(input('Input a number between 0 and 6: '))
        batting = random.randrange(7)
        print(f'Computer hit {batting} runs')
        if bowling != batting:
            bowl_status = 0
            first_batting_total = first_batting_total + batting
            print(f'Computer score is: {first_batting_total}')
        elif batting == bowling:
            bowl_status = 1
            print('Computer is OUT!')
            print(f'Your target is {first_batting_total}')
    print('You will now start batting.You will be out if you input number more than 6.')
    bat_status = 0
    second_batting_total = 0
    while bat_status == 0:
        batting = int(input('Input a number between 0 and 6: '))
        bowling = random.randrange(7)
        print(f'Computer bowled a {bowling}')
        if batting > 6:
            bat_status = 1
            print('YOU ARE OUT!')
            winner = 1
        elif batting != bowling:
            bat_status = 0
            second_batting_total = second_batting_total + batting
        if second_batting_total > first_batting_total:
            bat_status = 1
            winner = 0
        elif batting == bowling:
            bat_status = 1
            print('YOU ARE OUT!')
            winner = 1
        print(f'Your score is {second_batting_total}')

else:
    print('Unknown Pick detected. Pick only bat or bowl. Please restart the game.')

if winner == 0:
    print('YOU WIN!')
elif winner == 1:
    print('You lose. Better luck next time.')
else:
    print('The game is a TIE!')
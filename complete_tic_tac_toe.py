import numpy as np

def display_title():
	t1 = '         * * * * *   * * * * *   * * * * *\n             *           *       *\n             *           *       *\n             *           *       *\n             *       * * * * *   * * * * *'
	t2 = '         * * * * *   * * * * *   * * * * *\n             *       *       *   *\n             *       * * * * *   *\n             *       *       *   *\n             *       *       *   * * * * *'
	t3 = '         * * * * *   * * * * *   * * * * *\n             *           *       *       \n             *           *       * * * * *\n             *           *       *       \n             *       * * * * *   * * * * *'

	print('\n'+ '\n'+ '\n'+ '\n' +t1 + '\n'+ '\n'+ '\n'+ '\n' + t2 +'\n'+ '\n'+ '\n'+ '\n' + t3 + '\n'+ '\n'+ '\n'+ '\n' + 'Created by Daniel Evans')

def create_board():
	n0 = 'O'
	n1 = ' '
	n2 = ' '
	n3 = ' '
	n4 = ' '
	n5 = ' '
	n6 = ' '
	n7 = ' '
	n8 = ' '
	n9 = ' '

	s = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
	return s

def reset_board(s):
	l1 = '                               *     *   '
	l2 = '                           '+s[7]+'   *  '+s[8]+'  *   '+s[9]+' '
	l3 = '                         * * * * * * * * * *'
	l4 = '                           '+s[4]+'   *  '+s[5]+'  *   '+s[6]+' '
	l5 = '                           '+s[1]+'   *  '+s[2]+'  *   '+s[3]+' '

	board = l1+'\n'+l2+'\n'+l1+'\n'+l3+'\n'+l1+'\n'+l4+'\n'+l1+'\n'+l3+'\n'+l1+'\n'+l5+'\n'+l1
	return board

def intro():
	Intro = input('\n\n\n\nPress enter to start')

	Player1 = input('\n\n\n\nPlayer 1 what is your name?\n \n')

	Player2 = input('\n\n\n\nPlayer 2 what is your name?\n \n')

	return (Player1,Player2)

def going_first(players):
	import random

	r = random.randint(1,101)

	if r % 2 == 0:
		print('\n\n\n\n' + players[0] + ' goes first!')
		return (1,2)
	else:
		print('\n\n\n\n' + players[1] + ' goes first!')
		return (2,1)

def pick_shape(order):
	if order[0] == 1:
		marker = input('\n\n\n\nPlayer 1: Do you want to be X or O?\n \n').upper()
		if marker == 'X':
			return ('X','O')
		else:
			return ('O','X')
	else:
		marker = input('\n\n\n\nPlayer 2: Do you want to be X or O?\n \n').upper()
		if marker == 'X':
			return ('O','X')
		else:
			return ('X','O')

def place_shape(s, marker, position):
	s[int(position)] = marker
	return s

def check_space(s, position):
	return s[position] == ' '

def win_check(s,mark):
	return ((s[7] == mark and s[8] == mark and s[9] == mark) or
	(s[4] == mark and s[5] == mark and s[6] == mark) or 
    (s[1] == mark and s[2] == mark and s[3] == mark) or
    (s[7] == mark and s[4] == mark and s[1] == mark) or
    (s[8] == mark and s[5] == mark and s[2] == mark) or 
    (s[9] == mark and s[6] == mark and s[3] == mark) or 
    (s[7] == mark and s[5] == mark and s[3] == mark) or 
    (s[9] == mark and s[5] == mark and s[1] == mark))

def check_full(s):
	for i in np.arange(10):
		if check_space(s,i):
			return False
	return True

def player_position():
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space(s, int(position)):
		position = input('Choose position (1-9)')
	return int(position)

def retry():
	return input('Do you want to play again? (Y/N)').lower().startswith('y')






# Final Script to run the game

display_title()

Play_again = True

while Play_again:
	create_board()
	players=intro()
	order=list(going_first(players))
	shape=pick_shape(order)
	s=create_board()
	board=reset_board(s)
	print(players[(order[0]-1)] + ' time to play')
	game_on = True

	while game_on:
		if order[0] == 1:
			#Player1 turn

			print(board)
			position = player_position()
			s=place_shape(s, shape[0], position)
			board = reset_board(s)

			if win_check(s,shape[0]):
				print(board)
				print('Congrats you have won')
				game_on = False
			else:
				if check_full(s):
					print(board)
					print('Draw')
					break
				else:
					order[0] = 2

		else:
			#Player2 turn
			print(board)
			position = player_position()
			s=place_shape(s, shape[1], position)
			board = reset_board(s)

			if win_check(s,shape[1]):
				print(board)
				print('Congrats you have won')
				game_on = False
			else:
				if check_full(s):
					print(board)
					print('Draw')
					break
				else:
					order[0] = 1



	

	Play_again = retry()

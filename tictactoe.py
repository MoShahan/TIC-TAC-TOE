def check(B) :
	if (B['TL'] == B['TM'] == B['TR'] == 'X' or 
		B['ML'] == B['MM'] == B['MR'] == 'X' or
		B['LL'] == B['LM'] == B['LR'] == 'X' or
		B['TL'] == B['ML'] == B['LL'] == 'X' or
		B['TM'] == B['MM'] == B['LM'] == 'X' or
		B['TR'] == B['MR'] == B['LR'] == 'X' or
		B['TL'] == B['MM'] == B['LR'] == 'X' or
		B['TR'] == B['MM'] == B['LL'] == 'X') :
		
		print('\n')
		printB(theBoard)
		print('\n')
		print('Player X Wins')
		exit(0)

	elif (B['TL'] == B['TM'] == B['TR'] == 'O' or 
		  B['ML'] == B['MM'] == B['MR'] == 'O' or
		  B['LL'] == B['LM'] == B['LR'] == 'O' or
		  B['TL'] == B['ML'] == B['LL'] == 'O' or
		  B['TM'] == B['MM'] == B['LM'] == 'O' or
		  B['TR'] == B['MR'] == B['LR'] == 'O' or
		  B['TL'] == B['MM'] == B['LR'] == 'O' or
		  B['TR'] == B['MM'] == B['LL'] == 'O') :

		print('\n')
		printB(theBoard)
		print('\n')
		print('Player 0 Wins')
		exit(0)


def printB(x) :
	print(x['TL']+'|'+x['TM']+'|'+x['TR'])
	print('-+-+-')
	print(x['ML']+'|'+x['MM']+'|'+x['MR'])
	print('-+-+-')
	print(x['LL']+'|'+x['LM']+'|'+x['LR'])


def play() :
	turn = 'X'
	for i in range(9):
		print('\n')
		printB(theBoard)
		print('\n')
		print('Turn for ' + turn + '. Move on which space?')
		move = input()
		theBoard[move] = turn
		check(theBoard)
		if turn == 'X':
			turn = 'O'
		else:	
			turn = 'X'
	print('\n')
	printB(theBoard)
	print('\n')
	print('It is a DRAW Match')

theBoard = {'TL':' ','TM':' ','TR':' ','ML':' ','MM':' ','MR':' ','LL':' ','LM':' ','LR':' '}
print('Lets Play a Game of TIC TAC TOE')
play()

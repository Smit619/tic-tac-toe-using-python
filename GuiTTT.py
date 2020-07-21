#Tic Tac Toe

import tkinter as tk

root = tk.Tk()

root.title("Tic Tac Toe")

button_color = '#989898'
label_color = '#C0C0C0'


def start_game():

	global player
	global player_won
	global game_list
	global button_color
	global label_color

	player = 'X'

	player_won = False

	game_list = [["", "", ""],
			["", "", ""],
			["", "", ""]]


	def switch_player():

		global player

		if player == 'X':
			player = 'O'
		else:
			player = 'X'


	def button_clicked(x,y):

		global player
		global game_list

		label = tk.Label(root, text = player, bg  = label_color, height = 4, width = 10)
		label.grid(column = x, row = y)

		game_list[y][x] = player

		switch_player()

		result()


	def result():

		won_by_row()
		won_by_column()
		won_by_diagonal()
		game_tie()


	def won_by_row():

		global game_list
		global main_label
		global player_won

		if game_list[0][0] == game_list[0][1] == game_list[0][2] == 'X' :
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[1][0] == game_list[1][1] == game_list[1][2] == 'X':
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[2][0] == game_list[2][1] == game_list[2][2] == 'X':
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][0] == game_list[0][1] == game_list[0][2] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[1][0] == game_list[1][1] == game_list[1][2] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[2][0] == game_list[2][1] == game_list[2][2] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True


	def won_by_column():

		global game_list
		global main_label
		global player_won

		if game_list[0][0] == game_list[1][0] == game_list[2][0] == 'X' :
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][1] == game_list[1][1] == game_list[2][1] == 'X':
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][2] == game_list[1][2] == game_list[2][2] == 'X':
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][0] == game_list[1][0] == game_list[2][0] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][1] == game_list[1][1] == game_list[2][1] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][2] == game_list[1][2] == game_list[2][2] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True


	def won_by_diagonal():

		global game_list
		global main_label
		global player_won

		if game_list[0][0] == game_list[1][1] == game_list[2][2] == 'X':
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][2] == game_list[1][1] == game_list[2][0] == 'X':
			main_label = tk.Label(root, text = 'X won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][0] == game_list[1][1] == game_list[2][2] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True

		elif game_list[0][2] == game_list[1][1] == game_list[2][0] == 'O':
			main_label = tk.Label(root, text = 'O won', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')
			player_won = True


	def game_tie():

		global game_list
		global main_label
		global player_won
	 
		count = 0

		for row in game_list:
			for value in row:
				if value != '':
					count += 1

		if count == 9 and player_won == False:
			main_label = tk.Label(root, text = 'Game Tie', bg  = label_color, font = 30)
			main_label.grid(columnspan = 3, rowspan = 3, column = 0, row = 0, sticky = 'N'+'S'+'E'+'W')


	button_1 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(0 ,0))
	button_2 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(1 ,0))
	button_3 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(2 ,0))
	button_4 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(0 ,1))
	button_5 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(1 ,1))
	button_6 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(2 ,1))
	button_7 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(0 ,2))
	button_8 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(1 ,2))
	button_9 = tk.Button(root, height = 4, width = 10, bg = button_color, command = lambda : button_clicked(2 ,2))


	button_1.grid(column = 0, row = 0)
	button_2.grid(column = 1, row = 0)
	button_3.grid(column = 2, row = 0)
	button_4.grid(column = 0, row = 1)
	button_5.grid(column = 1, row = 1)
	button_6.grid(column = 2, row = 1)
	button_7.grid(column = 0, row = 2)
	button_8.grid(column = 1, row = 2)
	button_9.grid(column = 2, row = 2)


	start_new_game_button = tk.Button(root, text = 'New Game', bg = '#808080', command = start_game)
	start_new_game_button.grid(column = 0, row = 3, columnspan = 3, sticky = 'E'+'W')


	quit_button = tk.Button(root, text = 'Quit', bg = '#808080', command = root.destroy)
	quit_button.grid(column = 0, row = 4, columnspan = 3, sticky = 'E'+'W')


start_game()

root.mainloop()

import tkinter as tk
from game_logic import create_board, is_valid_move, make_move, undo_move, check_winner, is_draw
from ai import best_move

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe AI")
        self.board = create_board()
        self.difficulty = 'Hard'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.status_label = tk.Label(root, text="Your Turn (X)", font=('Arial', 14))
        self.status_label.grid(row=0, column=0, columnspan=3)
        self.create_buttons()
        self.create_menu()

    def create_buttons(self):
        for i in range(3):
              for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 32), width=4, height=1,
                                   bg='white', activebackground='lightgray',
                                   command=lambda i=i, j=j: self.click_cell(i, j))
                button.grid(row=i + 1, column=j)
                button.bind('<Enter>', lambda e, x=i, y=j: self.on_hover(x, y))
                button.bind('<Leave>', lambda e, x=i, y=j: self.on_leave(x, y))
                self.buttons[i][j] = button
    
    def on_hover(self, i, j):
        if self.board[i][j] == ' ':
            self.buttons[i][j].config(bg='lightblue')

    def on_leave(self, i, j):
        if self.board[i][j] == ' ':
            self.buttons[i][j].config(bg='white')

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        difficulty_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Difficulty", menu=difficulty_menu)
        for level in ['Easy', 'Medium', 'Hard']:
            difficulty_menu.add_command(label=level, command=lambda l=level: self.set_difficulty(l))
        menubar.add_command(label="Restart", command=self.restart_game)

    def set_difficulty(self, level):
        self.difficulty = level
        self.status_label.config(text=f"Difficulty set to {level}")

    def click_cell(self, i, j):
        if not is_valid_move(self.board, i, j):
            return
        make_move(self.board, i, j, 'X')
        self.update_buttons()
        winner = check_winner(self.board)
        if winner:
            self.end_game(f"{winner} wins!")
            return
        elif is_draw(self.board):
            self.end_game("It's a draw!")
            return


        self.status_label.config(text = "AI's Turn(0)")
        self.root.after(500, self.ai_move)
        
    def ai_move(self):
        move = best_move(self.board, self.difficulty)
        if move:
            make_move(self.board, move[0], move[1], 'O')
            self.update_buttons()
        winner = check_winner(self.board)
        if winner:
            self.end_game(f"{winner} wins!")
        elif is_draw(self.board):
            self.end_game("It's a draw!")
        else:
            self.status_label.config(text="Your Turn (X)")
        
    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                cell = self.board[i][j]
                btn = self.buttons[i][j]
                btn.config(text=cell)
                if cell == 'X':
                    btn.config(bg='lightgreen', disabledforeground='black')
                elif cell == 'O':
                    btn.config(bg='lightcoral', disabledforeground='black')
                
    def end_game(self, message):
        self.status_label.config(text=message)
        for row in self.buttons:
            for button in row:
                button.config(state = 'disabled')
        
    def restart_game(self):
        self.board = create_board()
        for row in self.buttons:
            for button in row:
                button.config(text ='',state = 'normal',bg='white')
        self.status_label.config(text = "Your Turn (X)")
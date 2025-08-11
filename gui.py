# import tkinter as tk
# from tkinter import messagebox
# from ai import best_move
# from game_logic import *

# class GameGUI:
#     def __init__(self):
#         self.window = tk.Tk() 
#         self.window.title("Tic Tac Toe AI")
#         self.window.resizable(False, False)

#         self.buttons = [[None for _ in range(3)] for _ in range(3)]
#         self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
#         self.current_player = PLAYER
#         self.difficulty = "hard"
#         self.mode = "ai"  # "ai" or "pvp"

#         self.create_mode_buttons()
#         self.create_difficulty_buttons()
#         self.create_restart_button()
#         self.create_board()
#         self.window.mainloop()

#     def create_mode_buttons(self):
#         frame = tk.Frame(self.window)
#         frame.pack(pady=10)

#         self.mode_label = tk.Label(frame, text="Mode: Human vs AI")
#         self.mode_label.pack(side=tk.LEFT, padx=5)

#         self.toggle_mode_btn = tk.Button(frame, text="Switch to Human vs Human", command=self.toggle_mode)
#         self.toggle_mode_btn.pack(side=tk.LEFT, padx=5)

#     def toggle_mode(self):
#         if self.mode == "ai":
#             self.mode = "pvp"
#             self.mode_label.config(text="Mode: Human vs Human")
#             self.toggle_mode_btn.config(text="Switch to Human vs AI")
#         else:
#             self.mode = "ai"
#             self.mode_label.config(text="Mode: Human vs AI")
#             self.toggle_mode_btn.config(text="Switch to Human vs Human")
#         self.restart_game()

#     def create_difficulty_buttons(self):
#         frame = tk.Frame(self.window)
#         frame.pack(pady=5)
#         for level in ["easy", "medium", "hard"]:
#             btn = tk.Button(frame, text=level.capitalize(), command=lambda l=level: self.set_difficulty(l))
#             btn.pack(side=tk.LEFT, padx=5)

#     def set_difficulty(self, level):
#         self.difficulty = level
#         self.restart_game()

#     def create_restart_button(self):
#         self.restart_button = tk.Button(self.window, text="Restart", command=self.restart_game)
#         self.restart_button.pack(pady=5)

#     def create_board(self):
#         frame = tk.Frame(self.window)
#         frame.pack()
#         for i in range(3):
#             for j in range(3):
#                 btn = tk.Button(frame, text="", width=10, height=4,
#                                 font=("Helvetica", 24), bg="white",
#                                 command=lambda row=i, col=j: self.player_move(row, col))
#                 btn.grid(row=i, column=j)
#                 btn.bind("<Enter>", lambda e, r=i, c=j: self.on_hover(r, c))
#                 btn.bind("<Leave>", lambda e, r=i, c=j: self.on_leave(r, c))
#                 self.buttons[i][j] = btn

#     def player_move(self, row, col):
#         if self.board[row][col] != EMPTY:
#             return

#         if self.mode == "ai":
#             if self.current_player != PLAYER:
#                 return  # prevent double-click during AI turn

#             self.board[row][col] = PLAYER
#             self.buttons[row][col].config(text=PLAYER, bg="lightgreen")

#             winner = check_winner(self.board)
#             if winner:
#                 self.show_result(f"{winner} wins!")
#                 return
#             elif is_draw(self.board):
#                 self.show_result("It's a draw!")
#                 return

#             self.current_player = AI
#             self.window.after(300, self.ai_move)
#             return

#         # PvP mode
#         self.board[row][col] = self.current_player
#         color = "lightgreen" if self.current_player == PLAYER else "lightcoral"
#         self.buttons[row][col].config(text=self.current_player, bg=color)

#         winner = check_winner(self.board)
#         if winner:
#             self.show_result(f"{winner} wins!")
#             return
#         elif is_draw(self.board):
#             self.show_result("It's a draw!")
#             return

#         self.current_player = PLAYER if self.current_player == AI else AI




#     def ai_move(self):
#         move = best_move(self.board, self.difficulty)
#         if move:
#             row, col = move
#             self.board[row][col] = AI
#             self.buttons[row][col].config(text=AI, bg="lightcoral")

#             winner = check_winner(self.board)
#             if winner:
#                 self.show_result(f"{winner} wins!")
#                 return
#             elif is_draw(self.board):
#                 self.show_result("It's a draw!")
#                 return

#         self.current_player = PLAYER




#     def restart_game(self):
#         self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
#         self.current_player = PLAYER
#         for i in range(3):
#             for j in range(3):
#                 self.buttons[i][j].config(text="", bg="white")

#     def on_hover(self, row, col):
#         if self.board[row][col] == EMPTY:
#             self.buttons[row][col].config(bg="lightblue")

#     def on_leave(self, row, col):
#         if self.board[row][col] == EMPTY:
#             self.buttons[row][col].config(bg="white")

#     def show_result(self, message):
#         messagebox.showinfo("Game Over", message)
#         self.restart_game()

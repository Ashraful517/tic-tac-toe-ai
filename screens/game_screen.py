import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import create_board, make_move, check_winner, is_draw
from ai import get_ai_move
import pygame

class GameScreen(tk.Frame):
    def __init__(self, master, mode, difficulty, on_restart):
        super().__init__(master)  # Important!
        self.master = master

        self.mode = mode
        self.difficulty = difficulty
        self.on_restart = on_restart

        self.current_player = "X"
        self.board = create_board()

        self.master.title("Tic Tac Toe Game")
        self.master.geometry("500x600")
        self.master.configure(bg="#E0F7FA")  # Light cyan background


        # Sound setup
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("assets/sounds/click.wav")

        self.label = tk.Label(self, text=f"Player {self.current_player}'s Turn", font=("Helvetica", 14), bg="#E0F7FA")
        self.label.pack(pady=10)

        self.frame = tk.Frame(self, bg="white")
        self.frame.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame, text="", width=10, height=5,
                font=("Helvetica", 22),
                bg="white", fg="black",
                activebackground="#D0EFFF",  # Light blue on click
                relief="raised",
                command=lambda row=i, col=j: self.on_click(row, col))

                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn
        # Ensure equal size for all rows and columns
        for i in range(3):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(i, weight=1)


    def on_click(self, row, col):
        # Prevent clicking during AI's turn
        if self.mode == "AI" and self.current_player == "O":
            return

        if self.board[row][col] != "":
            return

        self.make_turn(row, col)

        # If AI mode and it's now AI's turn after human move, trigger AI
        if self.mode == "AI" and self.current_player == "O":
            self.master.after(300, self.ai_turn)

    def make_turn(self, row, col):
        self.play_click()
        if make_move(self.board, row, col, self.current_player):
            self.update_ui()
            if self.check_game_over():
                return
            self.switch_player()

    def ai_turn(self):
        row, col = get_ai_move(self.board, self.difficulty)
        self.make_turn(row, col)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s Turn")

    def update_ui(self):
        for i in range(3):
            for j in range(3):
                mark = self.board[i][j]
                if mark == "X":
                    self.buttons[i][j].config(text="X", bg="lightgreen", fg="black")
                elif mark == "O":
                    self.buttons[i][j].config(text="O", bg="#FFCCCC", fg="black")  # light red
                else:
                    self.buttons[i][j].config(text="", bg="white")  # reset color if cleared


    def check_game_over(self):
        winner = check_winner(self.board)
        if winner:
            self.show_result(f"Player {winner} wins!")
            return True
        elif is_draw(self.board):
            self.show_result("It's a draw!")
            return True
        return False

    def show_result(self, msg):
        self.play_click()
        messagebox.showinfo("Game Over", msg)
        if (self.mode == "AI" and "X" in msg) or self.mode == "HUMAN":
            self.celebrate()
        self.on_restart()

    def celebrate(self):
        top = tk.Toplevel(self.master)
        top.title("🎉 Celebration!")
        top.geometry("350x180")
        top.configure(bg="#F3E5F5")  # Light purple background

        label = tk.Label(top, text="🎉 Congratulations! 🎉", font=("Helvetica", 20, "bold"), bg="#F3E5F5", fg="#4A148C")
        label.pack(expand=True, pady=40)

    def play_click(self):
        self.click_sound.play()

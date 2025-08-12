import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import create_board, make_move, check_winner, is_draw
from ai import get_ai_move
import pygame

class GameScreen(tk.Frame):
    def __init__(self, master, mode, difficulty, on_back):
        super().__init__(master)
        self.master = master
        self.mode = mode
        self.difficulty = difficulty
        self.on_back = on_back

        self.current_player = "X"
        self.board = create_board()

        self.master.title("Tic Tac Toe Game")
        center_window(self.master, 500, 550)
        self.master.configure(bg="white")

        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("assets/sounds/click.wav")

        # Top Frame for controls
        control_frame = tk.Frame(self, bg="white")
        control_frame.pack(fill="x")

        self.label = tk.Label(control_frame, text=f"Player {self.current_player}'s Turn",
                              font=("Helvetica", 14), bg="white")
        self.label.pack(side="left", padx=10, pady=10)

        back_btn = tk.Button(control_frame, text="← Back", command=self.on_back,
                             bg="#FF7043", fg="white", font=("Helvetica", 10, "bold"))
        back_btn.pack(side="right", padx=10)

        # Game board frame
        self.frame = tk.Frame(self, bg="white")
        self.frame.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame, text="", width=8, height=4,
                                font=("Helvetica", 20),
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def on_click(self, row, col):
        if self.mode == "AI" and self.current_player == "O":
            return
        if self.board[row][col] != "":
            return

        self.make_turn(row, col)
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
                    self.buttons[i][j].config(text=mark, bg="#FFCDD2", fg="black")  # Light red for X
                elif mark == "O":
                    self.buttons[i][j].config(text=mark, bg="#BBDEFB", fg="black")  # Light blue for O
                else:
                    self.buttons[i][j].config(text="", bg="white")  # Reset color


    def check_game_over(self):
        winner = check_winner(self.board)
        if winner:
            self.show_result(f"Player {winner} wins!")
            return True
        elif is_draw(self.board):
            self.show_result("It's a draw!")
            return True
        return False
    
    def celebrate(self):
        top = tk.Toplevel(self.master)
        top.title("🎉 Celebration!")
        center_window(top, 300, 150)
        top.configure(bg="#FFF9C4")  # Light yellow background

        tk.Label(
            top,
            text="🎉 Congratulations! 🎉",
            font=("Helvetica", 20, "bold"),
            fg="#D84315",
            bg="#FFF9C4"
        ).pack(expand=True, pady=20)

        tk.Button(
            top,
            text="OK",
            command=top.destroy,
            bg="#FF7043",
            fg="white",
            font=("Helvetica", 12, "bold")
        ).pack(pady=10)


    def show_result(self, msg):
        self.play_click()
        messagebox.showinfo("Game Over", msg)
        if "Player X wins" in msg and self.mode == "AI":
            self.celebrate()
        self.reset_game()
  # Stay in game screen, reset board

    def reset_game(self):
        self.board = create_board()
        self.current_player = "X"
        self.label.config(text=f"Player {self.current_player}'s Turn")
        self.update_ui()

    def play_click(self):
        self.click_sound.play()


def center_window(win, width, height):
    """Center a tkinter window on screen."""
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

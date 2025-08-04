import tkinter as tk
from gui import TicTacToeGame

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
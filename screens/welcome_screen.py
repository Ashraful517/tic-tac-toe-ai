import tkinter as tk

class WelcomeScreen(tk.Frame):
    def __init__(self, master, on_start):
        super().__init__(master)
        self.configure(bg="#FFDEE9")  # 💡 Vibrant pink/purple background

        title = tk.Label(self, text="🎮 Welcome to Tic-Tac-Toe!", 
                         font=("Helvetica", 20, "bold"), bg="#FFDEE9", fg="#4A148C")
        title.pack(pady=80)

        start_button = tk.Button(self, text="Start Game", 
                                 font=("Helvetica", 14), bg="#BA68C8", fg="white",
                                 command=on_start)
        start_button.pack(pady=20)




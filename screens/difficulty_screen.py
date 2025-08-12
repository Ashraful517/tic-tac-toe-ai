import tkinter as tk

class DifficultyScreen(tk.Frame):
    def __init__(self, master, mode, on_next, on_back):
        super().__init__(master)
        self.mode = mode
        self.on_next = on_next
        self.on_back = on_back

        tk.Label(self, text="Game Setup", font=("Helvetica", 16, "bold"), bg="#FFF3E0", fg="#E65100").pack(pady=20)

        if self.mode == "AI":
            self.diff_var = tk.StringVar(value="Easy")
            tk.Label(self, text="Select Difficulty", font=("Helvetica", 14), bg="#FFF3E0").pack()
            tk.Radiobutton(self, text="Easy", variable=self.diff_var, value="Easy", bg="#FFF3E0").pack()
            tk.Radiobutton(self, text="Medium", variable=self.diff_var, value="Medium", bg="#FFF3E0").pack()
            tk.Radiobutton(self, text="Hard", variable=self.diff_var, value="Hard", bg="#FFF3E0").pack()
        else:
            tk.Label(self, text="Tip: Take turns wisely!", font=("Helvetica", 12), wraplength=350, bg="#FFF3E0", fg="#BF360C").pack(pady=20)
            self.diff_var = None

        # Navigation buttons
        btn_frame = tk.Frame(self, bg="#FFF3E0")
        btn_frame.pack(pady=30)

        tk.Button(btn_frame, text="← Back", font=("Helvetica", 12), bg="#E65100", fg="white", command=self.on_back).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Start Game →", font=("Helvetica", 12), bg="#E65100", fg="white", command=self.submit).grid(row=0, column=1, padx=10)

    def submit(self):
    # If the game mode is AI, we pass the selected difficulty
    # If it's Human vs Human, we can still pass a default like "None"
        if self.mode == "AI":
            self.on_next(self.mode, self.diff_var.get())
        else:
            self.on_next(self.mode, "None")



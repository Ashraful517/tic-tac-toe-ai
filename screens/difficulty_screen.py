import tkinter as tk

class DifficultyScreen(tk.Frame):
    def __init__(self, master, mode, on_back, on_next):
        super().__init__(master, bg="#FFF3E0")  # Light orange
        self.mode = mode
        self.on_back = on_back
        self.on_next = on_next

        tk.Label(self, text="Game Setup", font=("Helvetica", 16, "bold"), bg="#FFF3E0", fg="#E65100").pack(pady=20)

        if self.mode == "AI":
            self.diff_var = tk.StringVar(value="Easy")
            tk.Label(self, text="Select Difficulty", font=("Helvetica", 14), bg="#FFF3E0").pack()
            tk.Radiobutton(self, text="Easy", variable=self.diff_var, value="Easy", bg="#FFF3E0").pack()
            tk.Radiobutton(self, text="Medium", variable=self.diff_var, value="Medium", bg="#FFF3E0").pack()
            tk.Radiobutton(self, text="Hard", variable=self.diff_var, value="Hard", bg="#FFF3E0").pack()
        else:
            tk.Label(self, text="Tip: In Human vs Human mode, take turns wisely!", font=("Helvetica", 12), wraplength=350, bg="#FFF3E0", fg="#BF360C").pack(pady=20)
            self.diff_var = None

        # Navigation buttons
        btn_frame = tk.Frame(self, bg="#FFF3E0")
        btn_frame.pack(pady=30)

        tk.Button(btn_frame, text="← Back", font=("Helvetica", 12), bg="#E65100", fg="white", command=self.on_back).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Start Game →", font=("Helvetica", 12), bg="#E65100", fg="white", command=self.submit).grid(row=0, column=1, padx=10)

    def submit(self):
        if self.mode == "AI":
            self.on_next(self.diff_var.get())
        else:
            self.on_next(None)

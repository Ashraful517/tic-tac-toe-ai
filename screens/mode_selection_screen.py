import tkinter as tk

class ModeSelectionScreen(tk.Frame):
    def __init__(self, master, on_mode_selected):
        super().__init__(master)
        self.configure(bg="#E3F2FD")  # 💡 Vibrant light blue

        self.on_mode_selected = on_mode_selected
        self.mode_var = tk.StringVar(value="AI")
        self.difficulty_var = tk.StringVar(value="Easy")

        title = tk.Label(self, text="Select Game Mode", font=("Helvetica", 16, "bold"),
                         bg="#E3F2FD", fg="#0D47A1")
        title.pack(pady=10)

        # Mode selection
        tk.Radiobutton(self, text="Human vs AI", variable=self.mode_var, value="AI",
                       command=self.toggle_difficulty, bg="#E3F2FD").pack()
        tk.Radiobutton(self, text="Human vs Human", variable=self.mode_var, value="HUMAN",
                       command=self.toggle_difficulty, bg="#E3F2FD").pack()

        # Difficulty options
        self.difficulty_frame = tk.Frame(self, bg="#E3F2FD")
        self.difficulty_frame.pack(pady=10)
        tk.Label(self.difficulty_frame, text="Select Difficulty", bg="#E3F2FD", font=("Helvetica", 12)).pack()
        tk.Radiobutton(self.difficulty_frame, text="Easy", variable=self.difficulty_var, value="Easy",
                       bg="#E3F2FD").pack()
        tk.Radiobutton(self.difficulty_frame, text="Medium", variable=self.difficulty_var, value="Medium",
                       bg="#E3F2FD").pack()
        tk.Radiobutton(self.difficulty_frame, text="Hard", variable=self.difficulty_var, value="Hard",
                       bg="#E3F2FD").pack()

        # Start button
        tk.Button(self, text="Start Game", command=self.submit, font=("Helvetica", 12),
                  bg="#1976D2", fg="white").pack(pady=20)

    def toggle_difficulty(self):
        if self.mode_var.get() == "AI":
            self.difficulty_frame.pack(pady=10)
        else:
            self.difficulty_frame.forget()

    def submit(self):
        self.on_mode_selected(self.mode_var.get(), self.difficulty_var.get())


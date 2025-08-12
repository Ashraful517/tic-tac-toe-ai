import tkinter as tk
from tkinter import ttk

class ModeSelectionScreen(tk.Frame):
    def __init__(self, master, on_back, on_next):
        super().__init__(master, bg="#E3F2FD")  # Light blue
        self.on_back = on_back
        self.on_next = on_next

        tk.Label(self, text="Select Game Mode", font=("Helvetica", 16, "bold"), bg="#E3F2FD", fg="#0D47A1").pack(pady=20)

        self.mode_var = tk.StringVar(value="AI")
        mode_dropdown = ttk.Combobox(self, textvariable=self.mode_var, values=["AI", "HUMAN"], state="readonly", font=("Helvetica", 12))
        mode_dropdown.pack(pady=10)

        # Navigation buttons
        btn_frame = tk.Frame(self, bg="#E3F2FD")
        btn_frame.pack(pady=30)

        tk.Button(btn_frame, text="← Back", font=("Helvetica", 12), bg="#1976D2", fg="white", command=self.on_back).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Next →", font=("Helvetica", 12), bg="#1976D2", fg="white", command=lambda: self.on_next(self.mode_var.get())).grid(row=0, column=1, padx=10)

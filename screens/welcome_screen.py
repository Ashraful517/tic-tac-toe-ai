import tkinter as tk

class WelcomeScreen(tk.Frame):
    def __init__(self, master, on_next):
        super().__init__(master, bg="#FCE4EC")  # Pink background
        self.on_next = on_next

        tk.Label(self, text="Welcome to Tic Tac Toe", font=("Helvetica", 20, "bold"), bg="#FCE4EC", fg="#880E4F").pack(pady=20)

        # Team info
        members = [
            ("Ashraful Alam Chowdhury", "ID: 1317"),
            ("Md Zubair Rahman", "ID: 1325"),
            ("Mahadi Hasan Rakib", "ID: 1321"),
            ("Rahma Ahmed Tonni","ID: 1307"),
            ("Sadia Akther","ID: 1305")
        ]

        for name, sid in members:
            tk.Label(self, text=name, font=("Helvetica", 14), bg="#FCE4EC").pack()
            tk.Label(self, text=sid, font=("Helvetica", 12), bg="#FCE4EC", fg="#555").pack()

        tk.Button(self, text="Next →", font=("Helvetica", 12), bg="#AD1457", fg="white", command=self.on_next).pack(pady=30)





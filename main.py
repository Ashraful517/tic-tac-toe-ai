import tkinter as tk
from screens.welcome_screen import WelcomeScreen
from screens.mode_selection_screen import ModeSelectionScreen
from screens.difficulty_screen import DifficultyScreen
from screens.game_screen import GameScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.center_window(400, 450)
        self.mode = None
        self.difficulty = None
        self.show_welcome_screen()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")

    def switch_frame(self, new_frame_class, *args):
        if hasattr(self, "current_frame") and self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)

    def show_welcome_screen(self):
        self.switch_frame(WelcomeScreen, self.show_mode_selection)

    def show_mode_selection(self):
        self.switch_frame(ModeSelectionScreen, self.show_welcome_screen, self.go_to_difficulty)

    def go_to_difficulty(self, mode):
        self.mode = mode
    # Pass mode, on_next callback (go_to_game), and on_back callback (show_mode_selection)
        self.switch_frame(DifficultyScreen, self.mode, self.go_to_game, self.show_mode_selection)
    
    def go_to_game(self, mode, difficulty):
        self.mode = mode
        self.difficulty = difficulty
        self.switch_frame(GameScreen, mode, difficulty, self.show_mode_selection)



    def show_game_screen(self, mode, difficulty):
        self.switch_frame(GameScreen, mode, difficulty, self.show_mode_selection)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
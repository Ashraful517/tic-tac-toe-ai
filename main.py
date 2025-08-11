import tkinter as tk
from screens.welcome_screen import WelcomeScreen
from screens.mode_selection_screen import ModeSelectionScreen
from screens.game_screen import GameScreen
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe - AI & Human Modes")
        self.geometry("400x500")
        self.resizable(False, False)

        self.current_frame = None
        self.show_welcome_screen()

    def switch_frame(self, new_frame_class, *args):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = new_frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)

    def show_welcome_screen(self):
        self.switch_frame(WelcomeScreen, self.show_mode_selection)


    def show_mode_selection(self):
        self.switch_frame(ModeSelectionScreen, self.show_game_screen)


    def show_game_screen(self, mode, difficulty):
        self.switch_frame(GameScreen, mode, difficulty, self.show_mode_selection)

if __name__ == "__main__":
    app = App()
    app.mainloop()

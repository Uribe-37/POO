from MainForm import MainForm
import tkinter as tk

class Friends:
    def __init__(self):
        pass

    def main(self):
        self.main_form = MainForm(tk.Tk())

if __name__ == "__main__":
    friends_app = Friends().main()
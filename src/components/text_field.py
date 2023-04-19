import tkinter as tk
import os

class TextField(tk.Text):
    def __init__(self, height: int = 700, width: int = 350) -> None:
        super().__init__(height = height, width = width)
        self.path = "save\\saved_text.txt"
    
    """
    Function for saving input from the text field. 
    """
    def save_input(self) -> None:
        text_input = self.get("1.0", "end-1c")

        if (os.path.exists("save") == False):
            os.makedirs("save")

        with open(self.path, "w+") as file:
            file.write(text_input)

    """
    Function for loading the input
    """
    def load_saved_input(self) -> None:
        if (os.path.exists("save") == False):
            os.makedirs("save")

        with open(self.path, "r+") as file:
            text = file.read()

            self.insert("1.0", text)

    """
    Function for clearing the text field.
    """
    def clear_text(self) -> None:
        self.delete("1.0","end")

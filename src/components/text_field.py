import tkinter as tk

from file_handling.file_handler import FileHandler
from file_handling.file_paths import FilePaths

class TextField(tk.Text):
    def __init__(self, height: int = 700, width: int = 350) -> None:
        super().__init__(height=height, width=width)
        file_path: str = FilePaths.SAVE_PATH.value
        self.file_handler: FileHandler = FileHandler(file_path)
    
    """
    Saves input from the text field. 
    """
    def save_input(self) -> None:
        text_input: str = self.get("1.0", "end-1c")
        self.file_handler.write(text_input)

    """
    Loads saved text and inserts it to the text field.
    """
    def load_saved_input(self) -> None:
        text: str = self.file_handler.read()
        self.insert("1.0", text)

    """
    Clears the text field.
    """
    def clear_text(self) -> None:
        self.delete("1.0","end")

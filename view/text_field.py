import tkinter as tk

from model.file_handling.file_handler import FileHandler
from model.file_handling.file_paths import FilePaths


class TextField(tk.Text):
    """Class to handle the text field operations like saving and loading text.
    Inherits from the tkinter Text class.
    """

    def __init__(self, height: int = 700, width: int = 350) -> None:
        """Initialize the TextField object with the height and width."""
        super().__init__(height=height, width=width)
        FILE_PATH: str = FilePaths.SAVE_PATH.value
        self.__file_handler: FileHandler = FileHandler(FILE_PATH)

    def save_input(self) -> None:
        """Save input from the text field."""
        text_input: str = self.get("1.0", "end-1c")
        self.__file_handler.write(text_input)

    def load_saved_input(self) -> None:
        """Load saved text and inserts it to the text field."""
        text: str = self.__file_handler.read()
        self.insert("1.0", text)

    def clear_text(self) -> None:
        """Clear the text field."""
        self.delete("1.0", "end")

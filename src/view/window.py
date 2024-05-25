import tkinter as tk
from tktooltip import ToolTip

from view.text_field import TextField
from model.file_handling.file_paths import FilePaths
from model.file_handling.file_handler import resource_path

class Window(tk.Tk):
    """Class to handle the main window of the application.
    Inherits from the tkinter Tk class.
    """
    def __init__(self) -> None:
        """Initialize the Window object."""
        super().__init__()
        
        self.title("Top Note")
        self.geometry("700x350")
        self.attributes("-topmost", True)

        relative_icon_path: str = FilePaths.ICON_PATH.value
        icon_photo: tk.PhotoImage = tk.PhotoImage(file=resource_path(relative_icon_path))
        self.iconphoto(False, icon_photo)

        self.text_field: TextField = TextField()

        self.button_frame: tk.Frame = tk.Frame(self)
        self.save_button: tk.Button = tk.Button(self.button_frame, text="Save", 
                                                command=self.text_field.save_input)
        self.load_button: tk.Button = tk.Button(self.button_frame, text="Load", 
                                                command=self.text_field.load_saved_input)
        self.clear_button: tk.Button = tk.Button(self.button_frame, text="Clear", 
                                                command=self.text_field.clear_text)

        self.put_components_on_grid()
        self.bind_shortcuts()
        self.set_tooltip_for_buttons()

    def put_components_on_grid(self) -> None:
        """Put the UI components on the grid."""
        self.save_button.grid(row=0, column=0, sticky=tk.NW)
        self.load_button.grid(row=0, column=1, sticky=tk.NW)
        self.clear_button.grid(row=0, column=2, sticky=tk.NW)

        self.button_frame.grid(row=0, sticky=tk.NW)
        self.text_field.grid(row = 1)

    def bind_shortcuts(self) -> None:
        """Bind the keyboard shortcuts to the respective functions."""
        self.bind("<Control-s>", lambda event: self.text_field.save_input())
        self.bind("<Control-l>", lambda event: self.text_field.load_saved_input())
        self.bind("<Alt-c>", lambda event: self.text_field.clear_text())
    
    def set_tooltip_for_buttons(self) -> None:
        """Set the tooltips for the buttons."""
        self.create_tooltips()
        self.raise_tooltips()

    def create_tooltips(self) -> None:
        """Create the tooltips for the buttons."""
        self.tooltip_for_save_button: ToolTip = ToolTip(self.save_button, "Saves text - CTRL+S")
        self.tooltip_for_load_button: ToolTip = ToolTip(self.load_button, "Loads text - CTRL+L")
        self.tooltip_for_clear_button: ToolTip = ToolTip(self.clear_button, "Clears text - ALT+C")

    def raise_tooltips(self) -> None:
        """Raise the tooltips to the topmost layer."""
        self.tooltip_for_save_button.wm_attributes("-topmost", 1)
        self.tooltip_for_load_button.wm_attributes("-topmost", 1)
        self.tooltip_for_clear_button.wm_attributes("-topmost", 1)

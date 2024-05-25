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

        self.__text_field: TextField = TextField()

        self.__button_frame: tk.Frame = tk.Frame(self)
        self.__save_button: tk.Button = tk.Button(self.__button_frame, text="Save", 
                                                  command=self.__text_field.save_input)
        self.__load_button: tk.Button = tk.Button(self.__button_frame, text="Load", 
                                                  command=self.__text_field.load_saved_input)
        self.__clear_button: tk.Button = tk.Button(self.__button_frame, text="Clear", 
                                                   command=self.__text_field.clear_text)

        self.__put_components_on_grid()
        self.__bind_shortcuts()
        self.__set_tooltip_for_buttons()

    def __put_components_on_grid(self) -> None:
        """Put the UI components on the grid."""
        self.__save_button.grid(row=0, column=0, sticky=tk.NW)
        self.__load_button.grid(row=0, column=1, sticky=tk.NW)
        self.__clear_button.grid(row=0, column=2, sticky=tk.NW)

        self.__button_frame.grid(row=0, sticky=tk.NW)
        self.__text_field.grid(row = 1)

    def __bind_shortcuts(self) -> None:
        """Bind the keyboard shortcuts to the respective functions."""
        self.bind("<Control-s>", lambda event: self.__text_field.save_input())
        self.bind("<Control-l>", lambda event: self.__text_field.load_saved_input())
        self.bind("<Alt-c>", lambda event: self.__text_field.clear_text())
    
    def __set_tooltip_for_buttons(self) -> None:
        """Set the tooltips for the buttons."""
        self.__create_tooltips()
        self.__raise_tooltips()

    def __create_tooltips(self) -> None:
        """Create the tooltips for the buttons."""
        self.__tooltip_for_save_button: ToolTip = ToolTip(self.__save_button, "Saves text - CTRL+S")
        self.__tooltip_for_load_button: ToolTip = ToolTip(self.__load_button, "Loads text - CTRL+L")
        self.__tooltip_for_clear_button: ToolTip = ToolTip(self.__clear_button, "Clears text - ALT+C")

    def __raise_tooltips(self) -> None:
        """Raise the tooltips to the topmost layer."""
        self.__tooltip_for_save_button.wm_attributes("-topmost", 1)
        self.__tooltip_for_load_button.wm_attributes("-topmost", 1)
        self.__tooltip_for_clear_button.wm_attributes("-topmost", 1)

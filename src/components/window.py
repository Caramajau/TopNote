import tkinter as tk
from tktooltip import ToolTip
import sys
import os

from components.text_field import TextField

class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Top Note")
        self.geometry("700x350")
        self.attributes("-topmost", True)

        icon_photo:tk.PhotoImage = tk.PhotoImage(file=resource_path("src\\resources\\t_icon.png"))
        self.iconphoto(False, icon_photo)

        self.text_field = TextField()

        self.button_frame:tk.Frame = tk.Frame(self)
        self.save_button:tk.Button = tk.Button(self.button_frame, text="Save", command=self.text_field.save_input)
        self.load_button:tk.Button = tk.Button(self.button_frame, text="Load", command=self.text_field.load_saved_input)
        self.clear_button:tk.Button = tk.Button(self.button_frame, text="Clear", command=self.text_field.clear_text)

        self.put_items_on_grid()
        self.bind_shortcuts()
        self.set_tooltip_for_buttons()


    def put_items_on_grid(self) -> None:
        self.save_button.grid(row = 0, column = 0, sticky = tk.NW)
        self.load_button.grid(row = 0, column = 1, sticky = tk.NW)
        self.clear_button.grid(row = 0, column = 2, sticky = tk.NW)

        self.button_frame.grid(row = 0, sticky=tk.NW)
        self.text_field.grid(row = 1)


    def bind_shortcuts(self) -> None:
        self.bind("<Control-s>", lambda event: self.text_field.save_input())
        self.bind("<Control-l>", lambda event: self.text_field.load_saved_input())
        self.bind("<Alt-c>", lambda event: self.text_field.clear_text())
    

    def set_tooltip_for_buttons(self) -> None:
        self.create_tooltips()
        self.raise_tooltips()

    def create_tooltips(self) -> None:
        self.tooltip_for_save_button:ToolTip = ToolTip(self.save_button, "Saves text - CTRL+S")
        self.tooltip_for_load_button:ToolTip = ToolTip(self.load_button, "Loads text - CTRL+L")
        self.tooltip_for_clear_button:ToolTip = ToolTip(self.clear_button, "Clears text - ALT+C")

    def raise_tooltips(self) -> None:
        self.tooltip_for_save_button.wm_attributes("-topmost", 1)
        self.tooltip_for_load_button.wm_attributes("-topmost", 1)
        self.tooltip_for_clear_button.wm_attributes("-topmost", 1)

def resource_path(relative_path:str) -> str:
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path:str = sys._MEIPASS
    except Exception:
        base_path:str = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

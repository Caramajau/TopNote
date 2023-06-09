import tkinter as tk
from tktooltip import ToolTip

from components.text_field import TextField

class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Top Note")
        self.geometry("700x350")
        self.attributes("-topmost", True)

        icon_photo = tk.PhotoImage(file="src\\resources\\t_icon.png")
        self.iconphoto(False, icon_photo)

        self.text_field = TextField()

        self.button_frame = tk.Frame(self)
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.text_field.save_input)
        self.load_button = tk.Button(self.button_frame, text="Load", command=self.text_field.load_saved_input)
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.text_field.clear_text)

        self.put_items_on_grid()
        self.bind_shortcuts()
        self.set_tooltip_for_buttons()


    def put_items_on_grid(self):
        self.save_button.grid(row = 0, column = 0, sticky = tk.NW)
        self.load_button.grid(row = 0, column = 1, sticky = tk.NW)
        self.clear_button.grid(row = 0, column = 2, sticky = tk.NW)

        self.button_frame.grid(row = 0, sticky=tk.NW)
        self.text_field.grid(row = 1)


    def bind_shortcuts(self):
        self.bind("<Control-s>", lambda event: self.text_field.save_input())
        self.bind("<Control-l>", lambda event: self.text_field.load_saved_input())
        self.bind("<Alt-c>", lambda event: self.text_field.clear_text())
    

    def set_tooltip_for_buttons(self):
        self.create_tooltips()
        self.raise_tooltips()

    def create_tooltips(self):
        self.tooltip_for_save_button = ToolTip(self.save_button, "Saves text - CTRL+S")
        self.tooltip_for_load_button = ToolTip(self.load_button, "Loads text - CTRL+L")
        self.tooltip_for_clear_button = ToolTip(self.clear_button, "Clears text - ALT+C")

    def raise_tooltips(self):
        self.tooltip_for_save_button.wm_attributes("-topmost", 1)
        self.tooltip_for_load_button.wm_attributes("-topmost", 1)
        self.tooltip_for_clear_button.wm_attributes("-topmost", 1)
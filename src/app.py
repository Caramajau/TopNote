from components.window import Window
import ctypes
import platform
import tkinter as tk

def main():
    __configure_task_bar_icon()

    the_window: tk.Tk = Window()
    the_window.mainloop()

def __configure_task_bar_icon() -> None:
    # From what I understand this is only necessary on Windows.
    if platform.system() == "Windows":
        # this changes so that the taskbar matches the window icon.
        my_app_id: str = "TopNote"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

if __name__ == "__main__":
    main()

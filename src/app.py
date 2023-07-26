from components.window import Window
import os
import ctypes
import platform

if (__name__ == "__main__"):
    if (os.path.exists("save") == False):
        os.makedirs("save")

    # From what I understand this is only necessary on Windows.
    if (platform.system() == "Windows"):
        # this changes so that the taskbar matches the window icon.
        my_app_id:str = "TopNote"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

    the_window = Window()
    the_window.mainloop()
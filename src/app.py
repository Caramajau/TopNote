from components.window import Window
import os
import ctypes

if __name__ == "__main__":
    if (os.path.exists("save") == False):
        os.makedirs("save")

    # this changes so that the taskbar matches the window icon.
    myappid = "mycompany.myproduct.subproduct.version" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    the_window = Window()
    the_window.mainloop()
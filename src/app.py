from components.window import Window
import os

if __name__ == "__main__":
    if (os.path.exists("save") == False):
        os.makedirs("save")

    the_window = Window()
    the_window.mainloop()
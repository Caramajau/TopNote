import os
import sys

class FileHandler:
    def __init__(self, file_path: str) -> None:
        self.FILE_PATH: str = file_path
    
    def write(self, text_to_save: str) -> None:
        self.__create_directory_if_not_exist()
        with open(self.FILE_PATH, "w+") as file:
            file.write(text_to_save)

    def __create_directory_if_not_exist(self) -> None:
        dir_name = os.path.dirname(self.FILE_PATH)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
    
    def read(self) -> str:
        try:
            return self.__read_file(self.FILE_PATH)
        
        except FileNotFoundError as e:
            print(f"Exception occurred: {e} \nFile at {self.FILE_PATH} has to be saved before loading")
            return ""

    def __read_file(self, file_path: str) -> str:
        with open(file_path, "r+") as file:
            text_content: str = file.read()
        return text_content

def resource_path(relative_path: str) -> str:
    # Source: https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path: str = sys._MEIPASS
    except Exception:
        base_path: str = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

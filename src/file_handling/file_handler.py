import os

class FileHandler:
    def __init__(self, file_path: str) -> None:
        self.FILE_PATH = file_path
    
    def write(self, text_to_save: str) -> None:
        self.__create_directory_if_not_exist()
        with open(self.FILE_PATH, "w+") as file:
            file.write(text_to_save)

    def __create_directory_if_not_exist(self):
        dir_name = os.path.dirname(self.FILE_PATH)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
    
    def read(self) -> str:
        with open(self.FILE_PATH, "r+") as file:
            text_content: str = file.read()

        return text_content

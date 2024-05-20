class FileHandler:
    def __init__(self, file_path: str) -> None:
        self.FILE_PATH = file_path
    
    def write(self, text_to_save: str) -> None:
        with open(self.FILE_PATH, "w+") as file:
            file.write(text_to_save)
    
    def read(self) -> str:
        with open(self.FILE_PATH, "r+") as file:
            text_content: str = file.read()

        return text_content

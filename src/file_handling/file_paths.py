from enum import Enum, unique
import os

@unique
class FilePaths(Enum):
    SAVE_PATH = os.path.join("save", "saved_text.txt")

from enum import Enum, unique
import os

@unique
class FilePaths(Enum):
    """Enum class for file paths."""
    SAVE_PATH = os.path.join("data", "saved_text.txt")
    ICON_PATH = os.path.join("resources", "t_icon.png")

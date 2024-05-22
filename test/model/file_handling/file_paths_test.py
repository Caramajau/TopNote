from parameterized import parameterized
import unittest as ut

from src.model.file_handling.file_paths import FilePaths

class FilePathsTest(ut.TestCase):
    file_path_test_cases = [(name, e.value) for name, e in FilePaths.__members__.items()]

    @parameterized.expand(file_path_test_cases)
    def test_path_is_not_none(self, _, path) -> None:
        self.assertIsNotNone(path)

    @parameterized.expand(file_path_test_cases)
    def test_path_is_string(self, _, path) -> None:
        self.assertIsInstance(path, str)
    
    @parameterized.expand(file_path_test_cases)
    def test_path_is_not_empty(self, _, path) -> None:
        self.assertNotEqual(path, "")

    def test_save_path_ends_with_saved_text_txt(self) -> None:
        save_path: str = FilePaths.SAVE_PATH.value
        self.assertTrue(save_path.endswith("saved_text.txt"))

    def test_icon_path_ends_with_t_icon_png(self) -> None:
        icon_path: str = FilePaths.ICON_PATH.value
        self.assertTrue(icon_path.endswith("t_icon.png"))

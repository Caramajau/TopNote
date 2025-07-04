import os

from parameterized import parameterized
import unittest as ut

from model.file_handling.file_paths import FilePaths


class FilePathsTest(ut.TestCase):
    file_path_test_cases: list[tuple[str, str]] = [
        (name, enum_member.value) for name, enum_member in FilePaths.__members__.items()
    ]
    invalid_chars: list[str] = [":", "*", "?", '"', "<", ">", "|"]

    @parameterized.expand(file_path_test_cases)
    def test_path_is_not_none(self, _, path) -> None:
        self.assertIsNotNone(path)

    @parameterized.expand(file_path_test_cases)
    def test_path_is_string(self, _, path) -> None:
        self.assertIsInstance(path, str)

    @parameterized.expand(file_path_test_cases)
    def test_path_is_not_empty(self, _, path) -> None:
        self.assertNotEqual(path, "")

    @parameterized.expand(file_path_test_cases)
    def test_path_contains_at_least_one_letter(self, _, path) -> None:
        self.assertRegex(path, r"[a-zA-Z]")

    @parameterized.expand(file_path_test_cases)
    def test_path_uses_correct_separator(self, _, path) -> None:
        self.assertIn(os.path.sep, path)

    @parameterized.expand(file_path_test_cases)
    def test_path_does_not_contain_invalid_characters(self, _, path) -> None:
        self.assertFalse(any(char in path for char in self.invalid_chars))

    def test_path_all_paths_are_unique(self) -> None:
        paths: list[str] = [enum_member.value for enum_member in FilePaths]
        self.assertEqual(len(paths), len(set(paths)))

    def test_save_path_ends_with_saved_text_txt(self) -> None:
        save_path: str = FilePaths.SAVE_PATH.value
        self.assertTrue(save_path.endswith("saved_text.txt"))

    def test_icon_path_ends_with_t_icon_png(self) -> None:
        icon_path: str = FilePaths.ICON_PATH.value
        self.assertTrue(icon_path.endswith("t_icon.png"))

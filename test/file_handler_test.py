import os

import unittest as ut

from model.file_handling.file_handler import FileHandler
from model.file_handling.file_handler import resource_path
from model.file_handling.file_paths import FilePaths


class FileHandlerTest(ut.TestCase):
    FILE_PATH: str = os.path.join("data", "test_file.txt")
    TEST_STRING: str = "This is a test text"
    ANOTHER_TEST_STRING: str = "This is another test text"

    def setUp(self) -> None:
        self.file_handler: FileHandler = FileHandler(self.FILE_PATH)

    def test_write_given_text_creates_file(self) -> None:
        self.file_handler.write(self.TEST_STRING)
        self.assertTrue(os.path.exists(self.FILE_PATH))

    def test_write_given_text_reads_same_text(self) -> None:
        self.file_handler.write(self.TEST_STRING)
        text: str = self.file_handler.read()
        self.assertEqual(text, self.TEST_STRING)

    def test_write_given_text_reads_same_text_after_overwriting(self) -> None:
        self.file_handler.write(self.TEST_STRING)
        self.file_handler.write(self.ANOTHER_TEST_STRING)
        text: str = self.file_handler.read()
        self.assertEqual(text, self.ANOTHER_TEST_STRING)

    def test_read_given_file_does_not_exist_returns_empty_string(self) -> None:
        text: str = self.file_handler.read()
        self.assertEqual(text, "")

    def test_resource_path_given_relative_path_ends_with_path(self) -> None:
        relative_path: str = FilePaths.ICON_PATH.value
        path: str = resource_path(relative_path)
        self.assertTrue(path.endswith(relative_path))

    def tearDown(self) -> None:
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)
        else:
            print("The file does not exist")

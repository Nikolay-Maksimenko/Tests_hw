import unittest
from yd_folder_creator import create_folder

class FolderCreatorTester(unittest.TestCase):
    def setUp(self) -> None:
        self.folder_creator = create_folder

    def test_code(self):
        code = create_folder('test_folder')
        self.assertTrue(str(code).startswith('2'), f'Ошибка! код ответа: {code}')

if __name__ == '__main__':
    unittest.main()
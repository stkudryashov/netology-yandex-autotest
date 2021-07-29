from unittest import TestCase

from api_token import api_token
from uploader import YaUploader


class TestYaUploader(TestCase):
    def setUp(self):
        self.uploader = YaUploader(api_token)

    def test_create_folder(self):
        status_code = self.uploader.create_folder('Cats')
        self.assertEqual(status_code, 201)

    def test_does_folder_exist(self):
        status_code = self.uploader.create_folder('Cats')
        self.assertEqual(status_code, 409)

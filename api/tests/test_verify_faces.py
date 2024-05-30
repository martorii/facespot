import os
import unittest
# Add path to sys if necessary
from utils.model import verify_faces


class TestVerifyFaces(unittest.TestCase):

    def setUp(self):
        # Load images from local files
        self.image1_path = os.path.join(os.path.dirname(__file__), 'images', 'Aaron_Peirsol_0001.jpg')
        self.image2_path = os.path.join(os.path.dirname(__file__), 'images', 'Aaron_Peirsol_0002.jpg')
        self.image3_path = os.path.join(os.path.dirname(__file__), 'images', 'Abba_Eban_0001.jpg')

    def test_verify_faces_match(self):
        # Test where faces match
        result = verify_faces(self.image1_path, self.image2_path)
        self.assertTrue(result, "Expected True, but got False")

    def test_verify_faces_no_match(self):
        # Test where faces do not match
        result = verify_faces(self.image1_path, self.image3_path)
        self.assertFalse(result, "Expected False, but got True")


if __name__ == '__main__':
    unittest.main()

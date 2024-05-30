from deepface import DeepFace
from PIL import Image
import io
import numpy as np


def verify_faces(img_1, img_2) -> bool:
    result = DeepFace.verify(
        img1_path=img_1,
        img2_path=img_2,
        enforce_detection=False,
        detector_backend='retinaface',
        model_name='VGG-Face',
        silent=True
    )
    return result['verified']


def convert_bytes_to_numpy(bytes_img: bytes) -> np.ndarray:
    return np.array(Image.open(io.BytesIO(bytes_img)))
import requests
import argparse
import numpy as np
from PIL import Image
from io import BytesIO

parser = argparse.ArgumentParser()
parser.add_argument('--image_path', type=str, required=True)
parser.add_argument('--background_path', type=str, required=True)

def test_upload_image(image_path, background_path):
    response = requests.post('http://0.0.0.0:8000/upload-image',
                            files={'image_file': open(image_path, 'rb'),
                                    'background_file': open(background_path, 'rb')})

    print('Received image with shape:', np.array(Image.open(BytesIO(response.content))).shape)
    return {'Successful'}

def main(args):
    response = test_upload_image(args.image_path, args.background_path)
    print(response)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)

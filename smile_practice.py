import os
import sys
import datetime
import cv2
from google.cloud import vision
from google.cloud.vision import types
import io

def save_frame_camera_cycle(device_num, dir_path, basename, cycle, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    client = vision.ImageAnnotatorClient()

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
        if n == cycle:
            n = 0
            file_name = '{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), ext)
            cv2.imwrite(file_name, frame)

            with io.open(file_name, 'rb') as image_file:
              content = image_file.read()
            image = types.Image(content=content)
            response = client.face_detection(image=image)

            faces = response.face_annotations

            print('\nFaces:')

            for face in faces:
                print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
                print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
                print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        n += 1

    cv2.destroyWindow(window_name)


save_frame_camera_cycle(0, 'data/temp', 'camera_capture_cycle', 300)

import numpy as np
import cv2
from mss import mss
from PIL import Image


top_offset = 0
left_offset = 0
width = 1280
height = 720
frame_size = (width ,height)
fps = 10
video_name = 'ScSh.mp4'
bounding_box = {'top': top_offset, 'left': left_offset, 'width': width, 'height': height}

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, fps, frame_size)

with mss() as sct:
    while True:
        sct_img = sct.grab(bounding_box)
        img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb, )
        cv2.imshow('screen', np.array(img))

        video.write(np.array(img))

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break


video.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
import socket
import sys
import pickle
import struct
from io import StringIO
import json

from io import BytesIO
import socketio



cap=cv2.VideoCapture(0)
clientsocket=socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# clientsocket.connect(('localhost',8485))
clientsocket.connect(('localhost',5000))

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

img_counter = 0

img_counter += 1

while(cap.isOpened()):
  ret,frame=cap.read()
  
  result, frame = cv2.imencode('.jpg', frame, encode_param)
  #    data = zlib.compress(pickle.dumps(frame, 0))
  data = pickle.dumps(frame, 0)
  size = len(data)

  # print(data)
  print("{}: {}".format(img_counter, size))

  s_data = struct.pack(">L", size) + data

  clientsocket.sendall(s_data)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
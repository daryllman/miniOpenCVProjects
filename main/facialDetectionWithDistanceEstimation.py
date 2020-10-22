import cv2
import sys
import math
import time
from os.path import dirname, abspath, join

brightnessVal = 0

#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade_file = join(dirname(dirname(abspath(__file__))),
                         "haarcascade", "haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier(face_cascade_file)

video_capture = cv2.VideoCapture(0)
print(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video recording
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("RecordedVid.mp4", fourcc, 60,
                      (frame_width, frame_height))

# Size of Face - estimated from diagonal of face rectangle
faceSize = 0

while True:
    time.sleep(0.5)
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate brightness
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    brightnessVal = hsv[2]
    print(brightnessVal)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        faceSize = math.sqrt(w**2 + h**2)
        print("FACE SIZE:" + str(faceSize))
        print(w, h)

    # Calculation: Distance from screen
    a = 82.894
    b = -0.00315962
    dist = a*math.e**(b*faceSize)
    distStr = str(round(dist, 2))

    # Check good distance from screen

    if (dist < 50):
        distStr += " (Bad)"
    else:
        distStr += " (Good)"

    # Display distance from screen
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame, "Vision 20/20", (0, 450),
                        font, 1, (240, 250, 0), 2, cv2.LINE_AA)
    frame = cv2.putText(frame, "Dist:", (0, 50), font, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, distStr, (100, 50), font,
                        1, (255, 255, 255), 1, cv2.LINE_AA)

    # Video Recording
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
out.release()
cv2.destroyAllWindows()
print("Video terminated")

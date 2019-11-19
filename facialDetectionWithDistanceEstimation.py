import cv2
import sys
import math

#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
print(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Size of Face - estimated from diagonal of face rectangle
faceSize = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
        print(w,h)
    
        
    # Calculation: Distance from screen
    a = 82.894
    b = -0.00315962
    dist = a*math.e**(b*faceSize)
    dist = str(round(dist,2))
    
    # Display distance from screen
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame,"Dist:", (0,50), font, 1, (255,255,255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, dist, (100,50), font, 1, (255,255,255), 1, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
print("Video terminated")
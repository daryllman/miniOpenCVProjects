import cv2

img = cv2.imread("lena.jpg", -1) #1: color, 0:grayscale, -1:unchanged


img = cv2.line(img, (0,0), (255,255), (255,0,0), 5) #topleftCorner to centre
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 5) #mid left to centre
img = cv2.rectangle(img, (384,0), (510,128), (0, 0, 255), 10 )
img = cv2.circle(img, (447,63), 63, (0, 255,0), -1 )


font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"OpenCv", (10,500), font, 4, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow("image", img)

k = cv2.waitKey(0)

if k ==21: #esc key
    cv2.destroyAllWindows()

elif k ==ord('s'): #s key is clicked
    cv2.imwrite("lena_copy.png", img)
    cv2.destroyAllWindows()
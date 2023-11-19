import cv2;
import numpy as np;

kamera = cv2.VideoCapture(0)


while (True):
    ret, video = kamera.read()
    hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 130, 15])
    upper_red = np.array([2, 200, 255])
    sb = cv2.inRange(hsv, lower_red, upper_red)
    renk = cv2.bitwise_and(video, video, mask=sb)
    cv2.imshow("Renkli", renk)
    cv2.imshow("Siyah-Beyaz",sb)
    if cv2.waitKey(50) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()

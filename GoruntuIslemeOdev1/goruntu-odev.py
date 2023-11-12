import cv2
import matplotlib.pyplot as plt
from numpy import zeros

goruntu=cv2.imread("goruntu.jpeg", 0)
cv2.imshow("goruntu.jpeg",goruntu)
histogram=zeros(256)
[gen,yuk] = goruntu.shape
for i in range(0,yuk):
    for x in range(0,gen):
        y=goruntu[x,i]
        histogram[y]+=1
plt.plot(histogram)
plt.show()
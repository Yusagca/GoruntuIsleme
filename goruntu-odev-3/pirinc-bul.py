import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pirinc.jpg', 0)
pencereBoy = 31
sabit = 40
kontur = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, pencereBoy, sabit)
plt.imshow(kontur)
cv2.imshow("Kontürlü", kontur)
cv2.waitKey()

deger = cv2.connectedComponentsWithStats(kontur, 8)[2]
ana = deger[1:, cv2.CC_STAT_AREA]

bolge_min, bolge_max = 345, max(list(ana))
mask2 = (bolge_min < ana) & (ana <= bolge_max)
konturlu_alan = np.mean(ana[mask2])

sayac = int(np.sum(np.round(ana / konturlu_alan)))

print('Pirinç Sayısı:', sayac)
import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = "WSI_image_analysis/tif/COLO320HSR_DAPI_Slide01_1-6s_50sh_stitch.tif"
image = "WSI_image_analysis/tif/COLO320HSR_DAPI_Slide02_1-6s_50sh_stitch.tif"
# image = "WSI_image_analysis/png/COLO320DM_0uM_HU_21d_01.converted.png"
img = cv2.imread(image, 1)
orig = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img = cv2.medianBlur(img, 7)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 3, param1=10, param2=15, minRadius=4, maxRadius=10)
# circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 30, param1=30, param2=55, minRadius=100, maxRadius=150)
detectedcircles = np.uint16(np.around(circles))
print(detectedcircles)
print(len(detectedcircles[0]))

for (x,y,r) in detectedcircles[0, :]:
    cv2.circle(orig, (x, y), r, (255, 190, 24), 2)
    # cv2.circle(orig, (x, y), 2, (255, 190, 24), 3)

# img = cv2.resize(img, None, fx=0.5, fy=0.5)
# orig = cv2.resize(orig, None, fx=0.5, fy=0.5)


cv2.imshow('original', orig)
cv2.imshow('grayscale', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

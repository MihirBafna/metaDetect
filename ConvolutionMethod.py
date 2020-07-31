import cv2
import numpy as np
import matplotlib.pyplot as plt

def mapcontours(contours):
    dict={}
    for contour in contours:
        print(contour)
        for pixel in contour:
            print(pixel)
            dict[pixel]=contour
    return dict

def fillcontours(img, contour, value):
    for pixel in contour:
        img[pixel] = value

def convolution(kernelsize, img,contourdictionary):
    newimg = img.copy()
    kernel = np.full((kernelsize, kernelsize), 1)
    rows = len(img)
    cols = len(img[0])
    print(f"------------------------------- \n Image size: \n ({rows},{cols}) \n------------------------------- \n Kernel matrix: \n {kernel} \n-------------------------------")
    for i in range(rows-kernelsize):
        if i%50==0:
            print(i)
        for j in range(cols-kernelsize):
            kerneloutput = 0
            for x in range(kernelsize):
                for y in range(kernelsize):
                    kerneloutput += img[i+x][j+y] * kernel[x][y]
            if kerneloutput/(kernelsize**2) >= 150 and contourdictionary[(i,j)]:
                # newimg[i+kernelsize//2][j+kernelsize//2] = 0
                fillcontours(newimg,contourdictionary[(i,j)],0)

            # elif kerneloutput/(kernelsize**2) <= 150:
            #     newimg[i+kernelsize//2][j+kernelsize//2] = 0
    return newimg


# image = "WSI_image_analysis/tif/COLO320HSR_DAPI_Slide01_1-6s_50sh_stitch.tif"
image = "WSI_image_analysis/tif/COLO320HSR_DAPI_Slide02_1-6s_50sh_stitch.tif"
image = "WSI_image_analysis/png/COLO320DM_0uM_HU_21d_01.converted.png"
image = "WSI_image_analysis/png/deletednuclei.jpg"
img = cv2.imread(image, 1)
img = img[0:len(img)//2, 0:len(img)//2]
orig = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binarized = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
contours = cv2.findContours(binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contourdict=mapcontours(contours)
print(contourdict) 
# convolutionimage = convolution(3,img,contourdict)
# orig = cv2.resize(orig, None, fx=0.5, fy=0.5)
# convolutionimage = cv2.resize(img, None, fx=0.5, fy=0.5)

# cv2.imshow('original', orig)
# cv2.imshow('convolution', convolutionimage)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 






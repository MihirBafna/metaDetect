import cv2
import numpy as np
import matplotlib.pyplot as plt


def convolution(kernelsize, img):
    newimg = img.copy()
    kernel = np.full((kernelsize, kernelsize), 1)
    rows = len(img)
    cols = len(img[0])
    print(f"Image size ({rows},{cols}) | Kernel matrix {kernel}")
    for i in range(rows-kernelsize):
        for j in range(cols-kernelsize):
            kerneloutput = 0
            for x in range(kernelsize):
                for y in range(kernelsize):
                    kerneloutput += img[i+x][j+y] * \
                        kernel[(i+x) % kernelsize][(j+y) % kernelsize]
            newimg[(i+kernelsize)//2][(j+kernelsize)//2] = kerneloutput
            print(kerneloutput)
    return newimg


# image = "WSI_image_analysis/tif/COLO320HSR_DAPI_Slide01_1-6s_50sh_stitch.tif"
image = "WSI_image_analysis/tif/COLO320HSR_DAPI_Slide02_1-6s_50sh_stitch.tif"
# image = "WSI_image_analysis/png/COLO320DM_0uM_HU_21d_01.converted.png"
img = cv2.imread(image, 1)
orig = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

convolutionimage = convolution(3,img)

orig = cv2.resize(orig, None, fx=0.5, fy=0.5)
convolutionimage = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow('original', orig)
cv2.imshow('convolution', convolutionimage)
cv2.waitKey(0)
cv2.destroyAllWindows()






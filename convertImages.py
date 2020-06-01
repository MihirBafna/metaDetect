from PIL import Image
import os


for file in os.listdir("WSI_image_analysis/tif/"):
    if file.endswith(".tif"):
        im = Image.open("WSI_image_analysis/tif/"+file)
        newim = file[:-3]+"png"
        print(newim)
        im.save("WSI_image_analysis/png/"+newim)


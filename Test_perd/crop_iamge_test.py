# from utils.locate_asset import crop_image
import os
from PIL import Image
corp=[]
i=1
area= (246,42,273,96)
def crop_iamge(image, area):
    ''' Uses PIL to crop an image, given its area.
    Input:
        image - PIL opened image
        Area - Coordinates in tuple (xmin, ymax, xmax, ymin) format '''
    img1 = Image.open(image)

    img = img1.crop(area)
    print(img.size)
    basewidth = 200
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    cropped_image = img.resize((basewidth, hsize), Image.ANTIALIAS)
    global i
    cropped_image.save("r" + str(i) + ".jpg", "JPEG", dpi=(300, 300))
    i += 1

    return cropped_image


cp=corp.append(crop_iamge('/tmp/pycharm_project_509/pancards/PAN-Card.jpg',area)

print(cp)

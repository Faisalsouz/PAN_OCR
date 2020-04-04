from subprocess import Popen, PIPE,check_output
from typing import Tuple,List
from PIL import Image
import json
import io
command= ['sudo','/usr/local/primestone/darknet/darknet', 'detector','test\
','/usr/local/primestone/darknet/data/custom_data/obj.data','/usr/local/primestone/darknet\
/data/custom_data/yolo-obj.cfg','/usr/local/primestone/darknet/backup/yolo-obj_best.weights','-ext_output', '-dont_show']
# detector test /data/custom_data/obj.data /data/custom_data/yolo-obj.cfg /backup/yolo-obj_last.weights -dont_show -map'
# s= subprocess.call('pwd')
# print(s)
# print(send_command.communicate())

def send_query(command):
    '''
    input: (list; every sapce in linux command is list element)\
    to send the command to darknet model via shh server\
    from remote.
    commnad is darknet command
    output: output is the output of darkent model with -ext_output argument
    '''
    send_job= Popen(command,stdin=PIPE,stdout=PIPE,universal_newlines=True)
    out= send_job.communicate('/media/primestone/test_samples/gava.jpg')
    return out[0]
    # output=send_job.stdout.readlines()
    # send_job.poll()



# send_query(command)


# next step is to extact the information form the output of the command line
line=open('example_ext_output.txt','r').read()

    # print(line)
    # print(line)
    #
    # inf=[]
    # for line in str(line).split('\n'):
    #     print(line)
    #     if "sign" in line:
    #         continue
    #     if "photo" in line:
    #         continue
    #     if 'left_x' in line:
    #         info=line.split()
    #         print(info[0])
    #         left_x = str(info[3])#int is removed just for test
    #         top_y = int(info[5])
    #         inf.append((info[0],left_x,top_y))
    #         # print(info[0],left_x,top_y)
    # print(inf)

'''
get the ouput resutls from the darknet send_job to ssh
and -ext_ouput argument of command print the coornate
and classes of iimage
'''
    #self.line=self.send_query(cmd)

inf = []
for line in str(line).split('\n'):

    if 'left_x' in line:
        info = line.split()
        class_id=info[0]
        #print(info)
        left_x = int(info[3])  # int is removed just for test
        top_y = int(info[5])
        width=int(info[7])
        height=int(info[9][:-1])
        inf.append((class_id, left_x, top_y,(left_x+width),(top_y+height)))



def coord_info_extractor(line: str) -> Tuple:
    ''' Extracts the information from a single line that contains a label.
        Input: line (string), a line that already contains the label
        Output: area (Tuple of four ints), which gives the area of the bounding box.
        '''

    ext_output = line.split()
    # print(ext_output)
    nameplate_confidence = ext_output[1]
    point_left_x = int(ext_output[3])
    point_top_y = int(ext_output[5])
    box_width = int(ext_output[7])
    box_height = int(ext_output[9][:-1])
    area = (point_left_x, point_top_y, (point_left_x + box_width), (point_top_y + box_height))
    return area


# line= 'project_id: 100%        (left_x: -inf   top_y:   10   width:  inf   height:    0)'
# l= line.split()
# print(l[:-1])


# a=coord_info_extractor('project_id: 100%        (left_x: 5   top_y:   10   width:  9   height:    5)')
# print(a)

#after having the tuple of  croping deimention from the fucntion coord_info_extractor whe need to \
#corp the all image for main image.
i=1
def crop_image(image, area: Tuple) -> object:
    ''' Uses PIL to crop an image, given its area.
    Input:
        image - PIL opened image
        Area - Coordinates in tuple (xmin, ymax, xmax, ymin) format '''
    img1 = Image.open(image)
    img = img1.crop(area)
    basewidth = 200
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    cropped_image = img.resize((basewidth, hsize), Image.ANTIALIAS)
    global i
   # cropped_image.save("r" + str(i) + ".jpg", "JPEG", dpi=(300, 300))
    i += 1

    return cropped_image
# test=[]
# test.append((a,crop_image('../pancards/PAN-Card.jpg',a)))
# print(test)

# next step would be using coord_info_extractor and image crop to gether with ouput of darkent\
#net model to get the  pair of iage and bounding box coordinates

def bbox_img_pairs(image, lines="") -> List:
    ''' Determines where an asset is in the picture, returning
     a set of coordinates, for the top left, top right, bottom
     left, and bottom right of the tag
     Returns:
     [(area, image)]
         Area is the coordinates of the bounding box
         Image is the image, opened by PIL.'''
    box_img_pairs = []
    # print(lines)
    for line in str(lines).split('\n'):
        if "sign" in line:
            continue
        if "photo" in line:
            continue
        # print(line)
        if "left_x" in line:
            # if 'photo' or 'sign' in line:
            # Extract the nameplate info
            # print(line)
            area = coord_info_extractor(line)
            # Open image
            box_img_pairs.append((area, crop_image(image, area)))

    # if box_img_pairs == []:
    #     logger.bad("No label found in image.")
    # else:
    #     logger.good("Found " + str(len(box_img_pairs)) + " label(s) in image.")

    return box_img_pairs
# bbx=bbox_img_pairs('../pancards/PAN-Card.jpg','project_id: 100%        (left_x: 22   top_y:   203   width:  154   height:    22)')

# Now after getting the bbox_image_pairs  we are ready to get the text extraction from the OCR engine
#import pyocr
import pytesseract
#import pyocr.builders
# tools= pyocr.get_available_tools()
# tool=tools[0]

# langs=tool.get_available_languages()
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def ocr(image:str,line:str) -> dict:
    '''
    input:
    image is image you want to crop and indentify
    line is ouput coordinate form darknet in Tuple
    output:
    dictionary
    '''

    #line='project_id: 100%        (left_x: 22   top_y:   203   width:  154   height:    22)'
    bbx= bbox_img_pairs(image,lines=line)
    output_dict={}
    for elm,i in zip(bbx,inf):
        #print(type(elm[1]))

        if i[1:]==elm[0]:
           # [0] is unravel the list that contain tuple and [:1] \

            im=elm[1]
            im.show()

        # is excluding the class, all coordinate tuple like(3,4,1,2)== to img_bbx pair that is like\
        #[(coordinate),img objt] 0 to unravel the list and 0 for tuple of coordinates
            text=pytesseract.image_to_string(elm[1],lang='eng')

            #im = elm[1]  # byte values of the image
            #im.show()
            #print(bbx[0][1])
            class_text=i[0]
            #print(class_text)
            output_dict[class_text]=[]
            output_dict[class_text].append(text)


    return output_dict

line= open('example_ext_output.txt','r').read()

imge='../pancards/PAN-Card.jpg'
a=ocr(image=imge,line=line)
#
# d={}
# for i in ['a','b','c','d','e','a','b']:
#     d[i]=[]
#     d[i].append('cd')
#     d[i].append('cd')
# print(d)



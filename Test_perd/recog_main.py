from subprocess import Popen, PIPE
from typing import Tuple,List
from PIL import Image
import pytesseract
from collections import defaultdict
import json

# from Test_perd.query_to_server import *
cmd= ['/usr/local/primestone/darknet/darknet', 'detector','test\
','/usr/local/primestone/darknet/data/custom_data/obj.data','/usr/local/primestone/darknet\
/data/custom_data/yolo-obj.cfg','/usr/local/primestone/darknet/backup/yolo-obj_best.weights','-ext_output', '-dont_show']
i=1
class RcogPipe():
    def __init__(self,command:str,pdf_pages:str) -> str:
        print('class: RecogPipe has received following command\n\
              \nand following:pdf pageNo:',command,pdf_pages)

        '''
        input: (list; every sapce in linux command is list element)\
        to send the command to darknet model via shh server\
        from remote.
        commnad is darknet command
        output: output is the output of darkent model with -ext_output argument
        '''
        send_job = Popen(command, stdin=PIPE, stdout=PIPE,stderr=PIPE, universal_newlines=True)
        self.out=send_job.communicate(pdf_pages)
        print('Darknet model internal view:\n',self.out[0])
        #return out[0]

    def  mapping(self):
        '''
        get the ouput resutls from the darknet send_job to ssh
        and -ext_ouput argument of command print the coornate
        and classes of iimage
        '''
        #self.line=self.send_query(cmd)
        self.line=self.out[0]
        inf = []
        for line in str(self.line).split('\n'):
            #print(line)
            # if "sign" in line:
            #     continue
            # if "photo" in line:
            #     continue
            if 'left_x' in line:
                info = line.split()
                class_id=info[0]
                #print(info)
                left_x = int(info[3])  # int is removed just for test
                top_y = int(info[5])
                width=int(info[7])
                height=int(info[9][:-1])
                inf.append((class_id, left_x, top_y,(left_x+width),(top_y+height)))
        return inf

    def coord_info_extractor(self,line: str) -> Tuple:
        ''' Extracts the information from a single line that contains a label.
            Input: line (string), a line that already contains the label
            Output: area (Tuple of four ints), which gives the area of the bounding box.
            '''
        #line=self.out[0] # output of darknet with argument -ext_output
        ext_output = line.split()
        # print(ext_output)
        nameplate_confidence = ext_output[1]
        point_left_x = int(ext_output[3])
        point_top_y = int(ext_output[5])
        box_width = int(ext_output[7])
        box_height = int(ext_output[9][:-1])
        area = (point_left_x, point_top_y, (point_left_x + box_width), (point_top_y + box_height))
        return area
    #i=1
    def crop_image(self,image, area: Tuple) -> object:
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
        #cropped_image.save("r" + str(i) + ".jpg", "JPEG", dpi=(300, 300))
        i += 1

        return cropped_image

    def bbox_img_pairs(self,image, lines="") -> List:
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
            if "left_x" in line:
                print('Found prediction data for given page')
                # if 'photo' or 'sign' in line:
                # Extract the nameplate info
                # print(line)
                area = self.coord_info_extractor(line)
                print('getting the coordinate data to crop the image')
                box_img_pairs.append((area, self.crop_image(image, area)))

        # if box_img_pairs == []:
        #     logger.bad("No label found in image.")
        # else:
        #     logger.good("Found " + str(len(box_img_pairs)) + " label(s) in image.")
        print('completing the bounding boxes and PIL croped images')
        return box_img_pairs

    def ocr(self,image):

        '''
        input:
        image is image you want to crop and indentify
        line is ouput coordinate form darknet in Tuple
        output:
        dictionary
        '''

        print('initialiizing the OCR')
        line=self.out[0]
        bbx = self.bbox_img_pairs(image, lines=line)
        output_dict = defaultdict(list)
        for elm, i in zip(bbx, self.mapping()):
            print('mapping the class and coordinates of cropped rectanges')

            if i[1:] == elm[0]:  # [0] is unravel the list that contain tuple and [:1] \

                # is excluding the class, all coordinate tuple like(3,4,1,2)== to img_bbx pair that is like\
                # [(coordinate),img objt] 0 to unravel the list and 0 for tuple of coordinates
                text = pytesseract.image_to_string(elm[1], lang='deu')
                # print(bbx[0][1])
                class_text = i[0]

                print('following class:Text has been extracted by ORC engine',class_text[0],text)
                output_dict[class_text].append(text)
                print('appending single page data dictionary')

        #json_dict=json.dumps(output_dict)
        print('single dictionary has been compated')
        return output_dict



#c=RcogPipe(cmd,'/media/primestone/test_samples/gava.jpg')
#c.send_query(cmd)

# dict=c.ocr('/media/primestone/test_samples/gava.jpg')
#
# print(dict)
# print(dict.values())
# import pandas as pd
# df=pd.DataFrame.from_dict(dict,orient='index')
# print(df)


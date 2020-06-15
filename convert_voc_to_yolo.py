from pprint import pprint
import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join
image_path=os.path.join(r'C:\Users\fkhalil\primeStone\deep_net\darknet\data\invoiceLabels\invoices-PascalVOC-export\JPEGImages')
xml_path=os.path.join(r'C:\Users\fkhalil\primeStone\deep_net\darknet\data\invoiceLabels\invoices-PascalVOC-export\Annotations')
main_path= os.path.join(r'C:\Users\fkhalil\primeStone\deep_net\darknet\data\invoiceLabels\invoices-PascalVOC-export')
output_path= os.path.join(r'C:\Users\fkhalil\primeStone\deep_net\darknet\data\invoiceLabels\yolo_converted')
obj_path= os.path.join(r'C:\Users\fkhalil\primeStone\deep_net\darknet\build\darknet\x64\data\obj')


classes = ['project_id', 'supplier', 'date', 'einzel_price', 'gesamt_price', 'invoice_details', 'pos', 'Menge', 'Beschreibung', 'fist_page', 'footer', 'einheit', 'table', 'summe', 'address', 'seite', 'LV', 'NT', 'header', 'ubertrag', 'customer_No']

def getImagesInDir(dir_path):
    '''
    The function returns the list of path names of all images location
    dir_path= path where all the iamges are stores.
    its path to folder not to single file
    '''
    image_list = []
    for filename in glob.glob(dir_path + '/*.jpg'):
        image_list.append(filename)

    return image_list
image= getImagesInDir(obj_path)
for lines in image:
    with open(os.path.join(r'C:\Users\fkhalil\primeStone\deep_net\darknet\build\darknet\x64\data','train.txt'),'a')as f:
        f.writelines(lines)
        f.writelines('\n')
    #
# def convert(size, box):
#     '''
#     converts the size and box value form xml voc file and then
#     retrun the center of object in term of x, y grid,
#     w and h is width and height of the object
#     '''
#     dw = 1./(size[0])
#     dh = 1./(size[1])
#     x = (box[0] + box[1])/2.0 - 1
#     y = (box[2] + box[3])/2.0 - 1
#     w = box[1] - box[0]
#     h = box[3] - box[2]
#     x = x*dw
#     w = w*dw
#     y = y*dh
#     h = h*dh
#     return (x,y,w,h)
#
# def convert_annotation(dir_path, output_path, image_path):
#     '''
#     dir_path= path to xml file located
#     out_path= the path where you wnat to save teh yolo format text files
#     image_path= where iamge of the voc label are saved
#     '''
#     basename = os.path.basename(image_path)
#     basename_no_ext = os.path.splitext(basename)[0]
#
#     in_file = open(dir_path + '/' + basename_no_ext + '.xml')
#     out_file = open(output_path +'/'+ basename_no_ext + '.txt', 'w')
#     tree = ET.parse(in_file)
#     root = tree.getroot()
#     size = root.find('size')
#     w = int(size.find('width').text)
#     h = int(size.find('height').text)
#
#     for obj in root.iter('object'):
#         difficult = obj.find('difficult').text
#         cls = obj.find('name').text
#         if cls not in classes or int(difficult)==1:
#             continue
#         cls_id = classes.index(cls)
#         xmlbox = obj.find('bndbox')
#         b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
#         bb = convert((w,h), b)
#         out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
# #
# # cwd = getcwd()
# #
# # for dir_path in dirs:
# #     full_dir_path = cwd + '/' + dir_path
# #     output_path = full_dir_path +'/yolo/'
# #
# #     if not os.path.exists(output_path):
# #         os.makedirs(output_path)
#
# image_paths = getImagesInDir(image_path)
# list_file = open(main_path + '.txt', 'w') # writing all the paths of image into text file as required by yolo
#
# for image_path in image_paths:
#     list_file.write(image_path + '\n')
#     convert_annotation(xml_path, output_path, image_path)
# list_file.close()
#
# print("Finished processing:")
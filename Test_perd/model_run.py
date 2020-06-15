from wand.image import Image as wi
import os
from pprint import pprint
from typing import Tuple,List,Type,TypeVar
from Test_perd.recog_main import *
import psycopg2
from Test_perd.config import  *
import pandas as pd
from postal.parser import parse_address

image=TypeVar('saved_iamges',bound='save_on_pathh')
def get_pdf(file_path:bytes)-> image:
    '''splitting pages of pdf into images:
    input= pdf file path or pdf bytes array
    output= list of all image blobs'''



    pdf_pages = []
    pdf = wi(blob=file_path, resolution=300)
    pdfimage = pdf.convert("jpg")

    i = 0
    for img in pdfimage.sequence:  # iterate over all pages extracted form the pdf doc
        page = wi(image=img)
        page.save(filename='./temp_pdfs/pdf_page_' + str(i) + '.jpg')
        pdf_pages.append('./temp_pdfs/pdf_page_' + str(i) + '.jpg')

        i += 1
    return pdf_pages

def model_run(dn_cmd,pdf_path:bytes) ->List:
    '''
    input= darkent model command\
    that will be fed into RecogPipe class
    pdf path has two effect one feeding into RecongPipe class in Darkent Command\
    second feeding the image to RecogPipe method 'ocr' as argument (image path to crop)
    output= json dictinary that append to existing json dictionary
    '''
    #supper_dict=defaultdict(list)
    supper_dict= []
    for index,pg in enumerate(get_pdf(pdf_path)):
        #pg= wi(image=pg)

        cls=RcogPipe(dn_cmd,pg)
        j_dict=cls.ocr(pg)
        page={'PageNo:':str(index)}
        m1={**page,**j_dict}
        if 'supplier:' in m1.keys():
            d=dict(parse_address(m1.get('supplier:')[0]))# seggregate the address.
            d=dict([(value, key) for key, value in d.items()])# correctng  the key value pair order
            m1['supplier:']=d
        if 'footer:' in m1.keys():
            ft = dict(parse_address(m1.get('footer:')[0]))
            ft = dict([(value, key) for key, value in ft.items()])
            m1['footer:'] = ft



        os.rename('./predictions.jpg', './predictions' + str(index) + '.jpg')
        supper_dict.append(m1)
        # supper_dict['pageNo'].append(index)
        # for k,v in dict.items():
        #     supper_dict[k].append(v)
        #     print('combining page data into json')
    #json_dic=json.dumps(supper_dict)
    print('Data from all PDF pages has been extracted successfully!')
    #pprint(supper_dict)
    return supper_dict
#############################################################
with open('/media/primestone/nachträge/DODEL/B1059250674/Daimler_NA16.pdf','rb')as f:#'/media/primestone/test_samples/heldele.pdf','rb'
    file=f.read()
    m=model_run(cmd,file)
    print(m)















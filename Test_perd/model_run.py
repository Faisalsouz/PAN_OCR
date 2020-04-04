from wand.image import Image as wi
import os
from pprint import pprint
from typing import Tuple,List,Type,TypeVar
from Test_perd.recog_main import *
image=TypeVar('saved_iamges',bound='save_on_pathh')
def get_pdf(file_path:str) -> image :
    '''
    splitting pages of pdf into iamges
    input= pdf file path or pdf byte file
    ouput= list of all save into tem_pdfs directory
    '''

   # pdf_pages=convert_from_path(file_path)
    pdf_pages=[]
    pdf = wi(filename=file_path, resolution=300)
    pdfimage = pdf.convert("jpg")
    i = 0
    for img in pdfimage.sequence:  # iterate over all pages extracted form the pdf doc
        page = wi(image=img)

        page=page.save(filename='./temp_pdfs/pdf_page_'+str(i)+'.jpg')
        # =blob=page.make_blob(format='jpeg')
        #pil_bytes=io.BytesIO(blob)
        # f_page=Image.open(blob)
        # pdf_pages.append(blob)
        pdf_pages.append('./temp_pdfs/pdf_page_'+str(i)+'.jpg')
        i+=1

    return pdf_pages

# pg=get_pdf('/media/primestone/test_samples/heldele.pdf')
# print(pg)

# for index in range(5):
#     print(index)
#     name=os.rename('./predictions.jpg','./predictions'+str(index)+'.jpg')
    # print(name)

def model_run(dn_cmd,pdf_path:str) ->dict:
    '''
    input= darkent model commande\
    that will be fed into RecogPipe class
    pdf path has two effect one feeding into RecongPipe class in Darkent Command\
    second feeding the image to RecogPipe method 'ocr' as argument (image path to crop)
    output= json dictinary that append to existing json dictionary
    '''
    supper_dict=defaultdict(list)
    for index,pg in enumerate(get_pdf(pdf_path)):
        print(pg,index)
        cls=RcogPipe(dn_cmd,pg)
        dict=cls.ocr(pg)
        for k,v in dict.items():
            supper_dict[k].append(v)
            print('combining page data into json')



       # os.rename('./predictions.jpg', './predictions' + str(index) + '.jpg')
    json_dic=json.dumps(supper_dict)
    print('Data from all PDF pages has been extracted successfully!')
    pprint(json_dic)
    return json_dic

m=model_run(cmd,'/media/primestone/test_samples/heldele.pdf')
print(m)
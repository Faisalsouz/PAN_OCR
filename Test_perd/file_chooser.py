from pprint import pprint
from wand.image import Image as wi
from wand.display import display
import os
from PIL import Image
import re
import psycopg2
from config import *
path= '/media/primestone/nachträge'
def get_pdf(file_path):
    '''splitting pages of pdf into iamges
    input= pdf file path or pdf bytes array
    ouput= list of all image blobs'''


    # pdf_pages=convert_from_path(file_path)
    pdf_pages = []
    pdf = wi(blob=file_path, resolution=600)
    pdfimage = pdf.convert("jpg")
    print(pdfimage)
    i = 0
    for img in pdfimage.sequence:  # iterate over all pages extracted form the pdf doc
        page = wi(image=img)
        save=page.convert('jpg')

        #page.save(filename='./temp_pdfs/pdf_page_' + str(i) + '.jpg')
        # =blob=page.make_blob(format='jpeg')
        # pil_bytes=io.BytesIO(blob)
        # f_page=Image.open(blob)
        # pdf_pages.append(blob)
        #pdf_pages.append('./temp_pdfs/pdf_page_' + str(i) + '.jpg')
        i += 1
        pdf_pages.append(save)
    return pdf_pages

# with open('NA01_pohler2.2.pdf','rb')as f:
#     file=f.read()
#     pdf=get_pdf(file)
#     for i in pdf:
#         Image.open(i)

    #######################backup of raw function##############
    # def get_pdf(file_path: str) -> image:
    #     '''
    #     splitting pages of pdf into iamges
    #     input= pdf file path or pdf byte file
    #     ouput= list of all save into tem_pdfs directory
    #     '''
    #
    #     # pdf_pages=convert_from_path(file_path)
    #     pdf_pages = []
    #     pdf = wi(filename=file_path, resolution=300)
    #     pdfimage = pdf.convert("jpg")
    #     i = 0
    #     for img in pdfimage.sequence:  # iterate over all pages extracted form the pdf doc
    #         page = wi(image=img)
    #
    #         page = page.save(filename='./temp_pdfs/pdf_page_' + str(i) + '.jpg')
    #         # =blob=page.make_blob(format='jpeg')
    #         # pil_bytes=io.BytesIO(blob)
    #         # f_page=Image.open(blob)
    #         # pdf_pages.append(blob)
    #         pdf_pages.append('./temp_pdfs/pdf_page_' + str(i) + '.jpg')
    #         i += 1
    #
    #     return pdf_pages



#database connection function:

def db_connect(dbqury):
    connection = psycopg2.connect(host=host ,database=database, user=username, password=passwords)
    cursor = connection.cursor()
    cursor.execute("set search_path to public;")
    cursor.execute(dbqury)
    #connection.commit()
    #result= pd.read_sql(dbqury,connection)
    return cursor.fetchall()
#q=db_connect("INSERT INTO client VALUES (nextval('client_sequence'), null, null, null, null, null, 'swilde', current_timestamp, 'swilde', current_timestamp) RETURNING client_id;")
#print(q)
#q= db_connect("SELECT * FROM client;")
#print(q)


#
# dict_1 ={'pos:': ['03.01.0020', '03.01.0010', '100'], 'invoice_details:': ['Nachtragsangebot Nr. 1 91702163'], 'Menge:': ['250', '100']}
#
# dict_2= {'invoice_details:': ['Nachtragsangebot Nr. 2 61702165'], 'pos:': ['03.02.0011', '03.04.0012'], 'Menge:': ['260']}
#
# pages=['page1','page2']
#
# supper_dict=[]
# for i,p in enumerate([dict_1,dict_2]):
#     page={'PageNo:':[str(i)]}
#     m1={**page,**p}
#     supper_dict.append(m1)
# for v in supper_dict:
#     print(v.keys())
#     if 'PageNo:' in v.keys():
#
#         print(v['PageNo:'])
out_dict= [{'PageNo:': '0', 'address:': ['Daimler AG, Bela-Barenyi-Straße \n 71059 Sindelfingen'], 'Beschreibung:':\
    ['anferigen,lefern und montieren.\nvon 5 Blechabdeckungen für\nRevisionszwecke-im EG Flur\n\nAbmasse ca 400x300x2mm mit UK'],\
            'einzel_price:': ['83,00']}, {'PageNo:': '1'}]


add='ınik = ITK Systemhaus Automation\nAmtsgericht Ulm: HRB 530646 - St.-Nr.: 28/63002/09062 = USt-IdNr.: DE 811368 083 » www.heldele.de\nrer: Wilhelm Wahl, Bernd Forstreuter, Rasmus Reutter, Jürgen Christ\nBanken IBAN SWIFT-BIC\n1 Uferstr. 40-50 - Tel. 07162.4002-0 - salach@heldele,de Kreissparkasse DE10 86105 0000 0004 0122 21 GOPSDESGXXX\ngen: Volksbank DE39 6106 0500 0140 9300 00 GENODES1VGP\nart - Julius-Hölder-Str. 39-41 : Tel. 07 11.7 2817-0 stuttgart@heldele,de BW-Bank AG DE9O 6005 0101 7871 5017 79 SOLADEST\nen - Jakob-Baumann-Str, 10 - Tel. 089.5177 77 49-0 . muenchen@heldele.de Commerzbank AG DE73 6104 0014 0181 5125 00 COBADEFFXXX'
#print(out_dict[0].keys())
from postal.parser import parse_address
# add=parse_address("jaimler AG\n{err Mangold\n\n\\bt. IPS/321_ HPC B 156\n11059 Sindelfingen")
# print('this is an address',type(add[0]))
# a ='this is wihous if statemtnet'
# if 'address:' in out_dict[0].keys():
#     print('addres value exits')
#     print(out_dict[0].get('address:')[0])
#     add=parse_address(add,language='german',country='germany')
#     print(dict(add))
#     out_dict[0]['address:']=dict(add)
#     print('this is new address',out_dict[0].values())
# par =parse_address(add,language='de',country='de')
# par=dict(par)
# par_new=dict([(value, key) for key, value in par.items()])
# # par=dict(par)
# print(par_new)

pos1=(251,2382,89,62)#x,y,w,h
pos2=(258,2722,83,64)
from typing import Tuple
def description_ext(pos1,pos2,offset=70):
    '''
    capturing the area between the two position to \n
    extract the data on rule based
    crop_x=left_x+width+offset# pos1
    crop_y= same as pos1
    crop_width= corp_x+(crop_x-2480)
    crop_hight= crop_y_p1+(crop_y_p1-left_x_p2)
    '''
    crop_x = pos1[0] + pos1[2] + offset  # pos1
    crop_y = pos1[1]
    crop_width = pos1[0] + (2400-crop_x)
    crop_hight = (pos2[1]-pos1[1])
    description_coord=(crop_x,crop_y,crop_x+crop_width,crop_y+crop_hight)# the way PIL accept the 4 coordinates
    return description_coord
print(pos1[0])

i=1
def crop_image(image, area: Tuple) -> object:
    ''' Uses PIL to crop an image, given its area.
    Input:
        image - PIL opened image
        Area - Coordinates in tuple (xmin, ymax, xmax, ymin) format '''
    print(area)
    img1 = Image.open(image)
    img = img1.crop(area)
    # basewidth = 200
    # wpercent = (basewidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    # cropped_image = img.resize((basewidth, hsize), Image.ANTIALIAS)
    global i
    img.save("cr_im" + str(i) + ".jpg", "JPEG", dpi=(300, 300))
    i+= 1

    return img
# print(description_ext(pos1,pos2))
#crop_image('./temp_pdfs/pdf_page_1.jpg',description_ext(pos1,pos2))

from postal.parser import parse_address

##############footer################4
add= ''' GEVA Gas- und Energieverteilungsanlagen GmbH\
Geschäftsführer: Edy-Karl Hohl, Timo Heidrich\n
Otto-Hahn-Str. 12 76275 Ettlingen\

Telefon: +49 7243 5248-0 Telefax: +49 7243 5248-48\
Sitz: Ettlingen E-Mail: anfrage@gevag  mbh.de\
internet: https://abce.de
'''


# rx= r'''(\b(Tel|Fax)\s*.*\d+|(\bE-?[mM]ail.*de)|([hH]ttps?:.*.de)|([Gg]esch[aä]ftsführer.+\S\s))'''
# address=re.sub(rx,'',add,re.UNICODE)
# print(address)
# # from postal.expand import expand_address
# norm_add=parse_address(address,language='de',country='germany')
# # add=expand_address(add,languages='de')
# print(norm_add)
def footer_text(string):
    '''
    input:
    any stirng contaiing address like data
    output:
    address dictionary
    '''
    rx = r'''(\b(Tel|Fax)\s*.*\d+|(\bE-?[mM]ail.*de)|([iI]nternet:?\s?[hH]ttps?:.*.de)|([Gg]esch[aä]ftsführer.+\S\s))'''
    s = re.sub(rx, '', string, re.UNICODE|re.MULTILINE)
    d = dict(map(reversed,parse_address(s, language='de', country='germany')))
    #n_d = dict([(value, key) for key, value in d.items()])
    return d
q= """SELECT recognition_image_patch FROM recognition where recognition_feature_name= 'DESC' and recognition_rule_based='True' LIMIT 1;"""


db=db_connect(q)
f=open('./image','wb').write(db[0][0])
read=open('image','rb').read()
print(read)
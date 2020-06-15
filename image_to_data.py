from wand.image import Image as wi
from PIL import Image
from pprint import pprint
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os
from pytesseract import Output
# import wand
import pandas as pd

image = pytesseract.image_to_pdf_or_hocr(Image.open(os.path.join(r'C:\Users\fkhalil\primeStone\docrecog\sampleDocs\convertedPdfs', 'AuftrLV_HELDELE_LV 1 Hauptumfang_W059 UT_Geb. 122-1 Randbau _Elektro.pdfPage_no128' + '.jpg')),\
                                         lang='deu',extension='pdf')
# df= pd.DataFrame(image)
# print(df)
print(image.save('abc'))
# with open(os.path.join(text_files, input_file + '.txt'), 'a+', encoding='utf-8') as f:
#     f.writelines(image)
# print('written the text of this {} image!'.format(img))
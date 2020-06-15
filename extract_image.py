from wand.image import Image as wi
from pprint import pprint
import os
pdf_path= os.path.join(r'C:\Users\fkhalil\InvRecog\Invoices')
out_path=os.path.join(r'C:\Users\fkhalil\InvRecog\Pdf2Img')
list_of_files= os.listdir(pdf_path)
processed_file= os.listdir(out_path)
import wand

processed_files=[fi.split('Page_no')[0] for fi in processed_file]
pprint(processed_files)
# pprint('These files are already processed',processed_files)
for file in list_of_files:
    if file in processed_files:
        print('file {} has already processed'.format(file))
    else:
        pdf = wi(filename=os.path.join(pdf_path,file), resolution=600)
        pdfimage = pdf.convert("jpeg")
        i = 1
        for img in pdfimage.sequence: #iterate over all pages extracted form the pdf doc
            page = wi(image=img)
            save_pages = 'Page_no' + str(i) + ".jpg"
            page=page.save(filename=os.path.join(out_path,file+save_pages))
            print('file{} and pages_No{} is processed'.format(file,save_pages))
            i+=1
####################################################


        # image = pytesseract.image_to_string(Image.open(os.path.join(converted_pdfs,input_file+'.jpg')), lang='deu')
        # with open(os.path.join(text_files, input_file+'.txt'), 'a+', encoding='utf-8') as f:
        #     f.writelines(image)
        # print('written the text of this {} image!'.format(img))
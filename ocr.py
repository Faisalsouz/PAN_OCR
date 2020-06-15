import PyPDF2 as pypdf
from PIL import Image
from pprint import pprint
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os

'''getting wroking directories of project'''

input_file='Nachtragsangebot Nr 2.pdf'
in_path=os.path.join(r"C:\Users\fkhalil\primeStone\docrecog\sampleDocs")
converted_pdfs=os.path.join(r"C:\Users\fkhalil\primeStone\docrecog\sampleDocs\convertedPdfs")
text_files= os.path.join(r"C:\Users\fkhalil\primeStone\docrecog\converterText")
processed_files= os.listdir(text_files)

'''checking if  text is already been converted or not'''
if input_file in processed_files:
    print('text file has already been generated')
else:
    '''checking if pdf file is scanned image of generated pdf file '''
    pdf_file = open(os.path.join(in_path, input_file), 'rb')
    page_data = pypdf.PdfFileReader(pdf_file).getPage(1)
    if'/Font' in page_data['/Resources']:
        print("Pdf contains text possibly:[trying to extract the text]")#, page_data['/Resources'].keys()
        t_pages=pypdf.PdfFileReader(pdf_file).getNumPages()#.extractText()
        for i in range(1,t_pages):
            content=pypdf.PdfFileReader(pdf_file).getPage(i).extractText()
            with open(os.path.join(text_files,input_file+'.txt'),'a+',encoding='utf-8')as f:
             f.writelines(content)

        # print(text)
    # else:
    #     list_of_docs= os.listdir(r"C:\Users\fkhalil\primeStone\docrecog\sampleDocs")#
    #     processed_files=[fi.split('Page_no')[0] for fi in converted_pdfs]
    #     pprint('These files are already processed',processed_files)
    #     for file in os.listdir(in_path):
    #         if file in processed_files:
    #             print('file {} has already processed'.format(file))
    else:
        # print('processing this {}'.format(file))
        from wand.image import Image as wi
        # import wand
        pdf = wi(filename=os.path.join(in_path,input_file), resolution=300)
        pdfimage = pdf.convert("jpeg")
        i = 1
        for img in pdfimage.sequence: #iterate over all pages extracted form the pdf doc
            page = wi(image=img)
            page=page.save(filename=os.path.join(converted_pdfs,input_file+'.jpg'))
            image = pytesseract.image_to_string(Image.open(os.path.join(converted_pdfs,input_file+'.jpg')), lang='deu')
            with open(os.path.join(text_files, input_file+'.txt'), 'a+', encoding='utf-8') as f:
                f.writelines(image)
            print('written the text of this {} image!'.format(img))



            # print(img[0])
            # save_pages = 'Page_no' + str(i) + ".jpg"
            # Image.open(page)

            # Image.open(page+'.jpg').()

            # print(type(page))
        #
        #     i +=1
        # print('done!')






    # print(page_data)
    # print(page_data['/Resources'] )#.get('/XObject'))


# #     #
# #
# # for i in converted_pdfs:
# #     image=pytesseract.image_to_string(Image.open(i),lang='deu')
# #     print(image)
# #
# # s='abc'
# # s1= 'file_name.bace.pdf'
# # path = os.path.join(converted_pdfs,s,s1)
# # print(path)
# pdf_file= open(os.path.join(in_path,input_file,),'rb')
# page_data=pypdf.PdfFileReader(pdf_file).getPage(1)
# print(page_data)
# print(page_data['/Resources'].get('/XObject'))
# if '/Font' in page_data['/Resources']:
#     print("[Info]: Looks like there is text in the PDF, contains:", page_data['/Resources'].keys())
# elif len(page_data['/Resources'].get('/XObject', {})) != 1:
#     print("[Info]: PDF Contains:", page_data['/Resources'].keys())

    # for obj in x_object:
    #     obj_ = x_object[obj]
    #     if obj_['/Subtype'] == '/Image':
    #         print("[Info]: PDF is image only")
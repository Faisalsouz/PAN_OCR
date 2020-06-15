import os
import invoice2data as ntd
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
file_name= 'NT_01.pdf'
temp_name='pdf2inv.py'
file_path= os.path.join(r'C:\Users\fkhalil\primeStone\docrecog\sampleDocs\EURO DIESEL\B1959500485',file_name)
temp_path=os.path.join(r'C:\Users\fkhalil\primeStone\docrecog\templates',temp_name)
print(file_path,temp_path)

templates = read_templates(temp_path)
result = extract_data(file_path, templates=templates)
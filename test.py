import os
from PyPDF2 import PdfFileMerger, PdfFileReader

directory=[]

path = input('Drag directory: ')
path = path[:-1]

for file in os.listdir(path):
    if file.endswith('.pdf'):
        directory.append(file)

directory.sort()

output = PdfFileMerger()
for i in directory:
    output.append(path+'/'+i)

output_name = input('Output filename: ')
output.write(output_name)

# THIS DOESN"T WORK
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

directory=[]

path = input('Drag directory: ')
path = path[:-1]

for file in os.listdir(path):
    if file.endswith('.pdf'):
        directory.append(file)

directory.sort()

merger = PdfFileMerger()
for n in directory:
    merger.append(n)

output_name = input('Output filename: ')
merger.write(output_name)


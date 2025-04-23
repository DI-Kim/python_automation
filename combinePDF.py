import PyPDF2
import os

os.chdir('C:\\Users\\user\\Downloads\\automate\\python_automation')

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfReader(pdfFile)

num_pages = len(reader.pages)
page = reader.pages[0]
page_text = page.extract_text()
# print(page_text)

# for i in range(num_pages):
#     print(reader.pages[i].extract_text())

# combine pdf file
pdfFile1 = open('meetingminutes1.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfReader(pdfFile1)
reader2 = PyPDF2.PdfReader(pdfFile2)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

outputFile = open('combinedminutes.pdf', 'wb')

writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdfFile1.close()
pdfFile2.close()
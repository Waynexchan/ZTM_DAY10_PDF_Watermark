import PyPDF2

input_file = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
water_mark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()
for page_no in range(input_file.getNumPages()):
    page = input_file.getPage(page_no)
    page.mergePage(water_mark.getPage(0))
    writer.addPage(page)

with open('Modified_page.pdf','wb') as new_file:
    writer.write(new_file)

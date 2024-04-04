from pathlib import Path
from PyPDF2 import PdfReader

pdf = PdfReader('hello_world.pdf')

page = pdf.pages[0]
#print(page)

pagestext = page.extract_text()
#print(type(pagestext))
"""
with Path('hello_world.pdf').open(mode='w') as output_file:
    text = ''
    for page in pdf.pages:
        text+=page.extract_text()
    output_file.write(text)
"""
'''
def extact():
    pdf = PdfReader('hello_world.pdf')
    page = pdf.pages[0]
    text = page.extract_text()
    return text

'''

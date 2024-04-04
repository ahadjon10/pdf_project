# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:34:15 2023

@author: user
"""

import PyPDF2

# Open the PDF file in read binary mode
with open('Passage1.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # Loop through all the pages and extract text
    for page_num in range(num_pages):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract text from the page
        text = page.extract_text()

        # Print the extracted text
        print(text)

# import re

# find = '(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))'

# email = re.findall(find, text)

# print(email)
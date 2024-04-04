import PyPDF2

# Open the PDF file in read binary mode
with open('cv.pdf', 'rb') as pdf_file:
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
        print(type(text))

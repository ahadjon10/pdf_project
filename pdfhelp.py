# import PyPDF2

# pdfObj = open('hello_world.pdf', 'rb')

# PyPDF2.PdfFileReader(
#     pdfObj, strict = True,
#  warndest=True, overwriteWarnings=True
# #  )
# After making this change, your code should work without the deprecation error. Make sure you've imported the PdfReader class from PyPDF2 at the beginning of your script. Here's an example:
from PyPDF2 import PdfReader

# Rest of your code...



# from PyPDF2 import PdfFileReader
from tkinter import *
from tkinter import filedialog

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#D9653B')

def choose_pdf():
      filename = filedialog.askopenfilename(
            initialdir = "/",   # for Linux and Mac users
          # initialdir = "C:/",   for windows users
            title = "Select a File",
            filetypes = (("PDF files","*.pdf*"),("all files","*.*")))
      if filename:
          return filename


def read_pdf():
    filename = choose_pdf()
    reader = PdfReader(filename)
    pageObj = reader.getNumPages()
    for page_count in range(pageObj):
        page = reader.getPage(page_count)
        page_data = page.extractText()
        textbox.insert(END, page_data)

def copy_pdf_text():
    content = textbox.get(1.0, "end-1c")
    ws.withdraw()
    ws.clipboard_clear()
    ws.clipboard_append(content)
    ws.update()
    ws.destroy()


textbox = Text(
    ws,
    height=13,
    width=40,
    wrap='word',
    bg='#D9BDAD'
)
textbox.pack(expand=True)

Button(
    ws,
    text='Choose Pdf File',
    padx=20,
    pady=10,
    bg='#262626',
    fg='white',
    command=read_pdf
).pack(expand=True, side=LEFT, pady=10)

Button(
    ws,
    text="Copy Text",
    padx=20,
    pady=10,
    bg='#262626',
    fg='white',
    command=copy_pdf_text
).pack(expand=True, side=LEFT, pady=10)


ws.mainloop()


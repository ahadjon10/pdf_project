from fpdf import FPDF

pdf = FPDF('L', 'mm', 'Letter')

pdf.add_page()

pdf.set_font('times', 'BU', 14)
pdf.set_text_color(220, 50, 50)
pdf.cell(80, 20, 'Salom XATOBOSH!!!', border=True)
pdf.cell(100, 40, 'How times change!!! ', border=True)
pdf.cell(120, 60, 'Xayr XATOBOSH!!!', border=True)
pdf.output('1.pdf')

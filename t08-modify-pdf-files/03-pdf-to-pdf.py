from PyPDF2 import PdfWriter
from pathlib import Path

pdf_writer = PdfWriter()
pdf_writer.add_blank_page(width=72, height=72)

with Path("blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

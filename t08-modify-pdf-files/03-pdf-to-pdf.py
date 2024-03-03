from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path


# ******************************************* FIRST *******************************************
# Adding a blank page
# pdf_writer = PdfWriter()
# pdf_writer.add_blank_page(width=72, height=72)

# with Path("blank.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# ******************************************* SECOND *******************************************
# Taking a page from a pdf and adding it to a new empty one
# pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"
# pdf_reader = PdfReader(str(pdf_path))
# first_page = pdf_reader.pages[0]
# pdf_writer = PdfWriter()
# pdf_writer.add_page(first_page)

# new_pdf_path = Path.cwd() / "first_page.pdf"
# with new_pdf_path.open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# ******************************************* THIRD *******************************************
# Extracting multiple pages from a pdf and add them to a new empty one
# pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"
# pdf_reader = PdfReader(str(pdf_path))

# pdf_writer = PdfWriter()
# # for num_page in range(4):
# #     page = pdf_reader.pages[num_page]
# #     pdf_writer.add_page(page)

# for page in pdf_reader.pages[1:4]:
#     pdf_writer.add_page(page)

# new_pdf_path = Path.cwd() / "first_chapter.pdf"
# with new_pdf_path.open(mode="wb") as output_file:
#     pdf_writer.write(output_file)


# ******************************************* FOURTH *******************************************
# Using shortcut for copying and entire pdf
pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"
pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()
pdf_writer.append_pages_from_reader(pdf_reader)
with Path("Pride_and_Prejudice_copy.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

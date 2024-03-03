from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

pdf_reader = PdfReader(str("Pride_and_Prejudice.pdf"))

# ***********
# Exercise 1
# 1. Extract the last page from the Pride_and_Prejudice.pdf file and save
# it to a new file called last_page.pdf in your home directory.
# ***********

# last_page_num = len(pdf_reader.pages) - 1
# last_page = pdf_reader.pages[last_page_num]
# pdf_writer = PdfWriter()
# pdf_writer.add_page(last_page)

# with Path("p&p_last_page.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# ***********
# Exercise 2
# 2. Extract all pages with even numbered indices from the Pride_-
# and_Prejudice.pdf and save them to a new file called every_other_-
# page.pdf in your home directory.
# ***********

# pdf_writer = PdfWriter()

# for i in range(len(pdf_reader.pages)):
#     num_page = (i + 1) % 2
#     if num_page == 0:
#         pdf_writer.add_page(pdf_reader.pages[i])

# with Path("p&p_every_other_page.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# ***********
# Exercise 3
# 3. Split the Pride_and_Prejudice.pdf file into two new PDF files. The
# first file should contain the first 150 pages, and the second file
# should contain the remaining pages. Save both files in your home
# directory as part_1.pdf and part_2.pdf
# ***********

# Start by creating two new PdfFileWriter instances.
pdf_writer_p1 = PdfWriter()
pdf_writer_p2 = PdfWriter()

# Create two new iterables containing the correct pages.
part1_pages = pdf_reader.pages[:150]
part2_pages = pdf_reader.pages[150:]

# Add the pages to their corresponding writers.
for page in part1_pages:
    pdf_writer_p1.add_page(page)

for page in part2_pages:
    pdf_writer_p2.add_page(page)

# Now write the contents of each writer to the files `part_1.pdf` and
# `part_2.pdf` in your home directory.
with Path("p&p_part_1.pdf").open(mode="wb") as output_file:
    pdf_writer_p1.write(output_file)

with Path("p&p_part_2.pdf").open(mode="wb") as output_file:
    pdf_writer_p2.write(output_file)

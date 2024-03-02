from PyPDF2 import PdfReader
from pathlib import Path

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"
pdf = PdfReader(str(pdf_path))
print(f"Num pages: {len(pdf.pages)}")
print(f"Doc Info: {pdf.metadata.title}")  # type: ignore

first_page = pdf.pages[9]
text_page = first_page.extract_text()
print(text_page)

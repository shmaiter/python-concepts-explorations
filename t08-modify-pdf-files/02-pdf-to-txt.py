from PyPDF2 import PdfReader
from pathlib import Path

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"
pdf = PdfReader(str(pdf_path))

txt_path = Path.cwd() / "Pride_and_Prejudice.txt"
with txt_path.open(mode="w", encoding="utf-8", newline="\n") as file:

    file.write(
        f"{pdf.metadata.title} \n"  # type: ignore
        f"Number of pages: {len(pdf.pages)}"
    )

    for page in (pdf.pages):
        text = page.extract_text()
        file.write(text)

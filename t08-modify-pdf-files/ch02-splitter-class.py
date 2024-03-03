from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


class PdfFileSplitter:

    def __init__(self, pdf_path) -> None:
        self.pdf_path = Path(pdf_path)
        self.reader = PdfReader(str(pdf_path))
        self.writer1 = PdfWriter()
        self.writer2 = PdfWriter()

    def split(self, breakpoint):
        self.pages_p1 = self.reader.pages[:breakpoint]
        self.pages_p2 = self.reader.pages[breakpoint:]

    def write(self, new_path):
        filename = self.pdf_path.stem

        for page in self.pages_p1:
            self.writer1.add_page(page)

        for page in self.pages_p2:
            self.writer2.add_page(page)

        with Path(new_path / (filename + "_p1.pdf")).open(mode="wb") as output_file:
            self.writer1.write(output_file)

        with Path(new_path / (filename + "_p2.pdf")).open(mode="wb") as output_file:
            self.writer2.write(output_file)


pdf_splitter = PdfFileSplitter("Pride_and_Prejudice.pdf")
pdf_splitter.split(15)
pdf_splitter.write(Path.cwd())

# print(Path("Pride_and_Prejudice.pdf").stem)

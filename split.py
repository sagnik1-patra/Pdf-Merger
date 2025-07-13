from PyPDF2 import PdfReader, PdfWriter
from rich import print

def split_pdf(file, pages):
    try:
        reader = PdfReader(file)
        writer = PdfWriter()
        start, end = map(int, pages.split('-'))
        for i in range(start - 1, end):
            writer.add_page(reader.pages[i])
        output = f"split_{start}-{end}.pdf"
        with open(output, "wb") as f:
            writer.write(f)
        print(f"[green]✅ Split pages {start}-{end} into {output}")
    except Exception as e:
        print(f"[red]❌ Error: {e}")


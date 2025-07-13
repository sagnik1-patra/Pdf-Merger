from PyPDF2 import PdfReader, PdfWriter
from rich import print

def add_watermark(input_pdf, watermark_pdf, output):
    try:
        reader = PdfReader(input_pdf)
        watermark = PdfReader(watermark_pdf).pages[0]
        writer = PdfWriter()

        for page in reader.pages:
            page.merge_page(watermark)
            writer.add_page(page)

        with open(output, "wb") as f:
            writer.write(f)
        print(f"[green]✅ Watermark added to {output}")
    except Exception as e:
        print(f"[red]❌ Error: {e}")


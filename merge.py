from PyPDF2 import PdfMerger
from rich import print

def merge_pdfs(files, output):
    merger = PdfMerger()
    try:
        for pdf in files:
            merger.append(pdf)
        merger.write(output)
        merger.close()
        print(f"[green]✅ Merged PDFs into {output}")
    except Exception as e:
        print(f"[red]❌ Error: {e}")


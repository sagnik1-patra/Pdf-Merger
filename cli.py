import argparse
from pdf_tool import merge, split, watermark

def main():
    parser = argparse.ArgumentParser(
        description="🛠 PDF Toolkit - Merge, Split, and Watermark PDFs"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Merge
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs")
    merge_parser.add_argument("files", nargs='+', help="PDF files to merge")
    merge_parser.add_argument("-o", "--output", default="merged.pdf", help="Output filename")

    # Split
    split_parser = subparsers.add_parser("split", help="Split a PDF by page range")
    split_parser.add_argument("file", help="PDF file to split")
    split_parser.add_argument("pages", help="Page range (e.g., 1-3)")

    # Watermark
    watermark_parser = subparsers.add_parser("watermark", help="Add watermark to PDF")
    watermark_parser.add_argument("file", help="PDF file to watermark")
    watermark_parser.add_argument("watermark", help="Watermark PDF file")
    watermark_parser.add_argument("-o", "--output", default="watermarked.pdf", help="Output filename")

    args = parser.parse_args()

    if args.command == "merge":
        merge.merge_pdfs(args.files, args.output)
    elif args.command == "split":
        split.split_pdf(args.file, args.pages)
    elif args.command == "watermark":
        watermark.add_watermark(args.file, args.watermark, args.output)
    else:
        parser.print_help()


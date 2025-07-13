A simple yet powerful command-line tool to manage PDF files. With this toolkit, you can merge, split, and add watermarks to PDF documents right from your terminal.

No need for bulky software—just pure productivity.

 Features
 Merge multiple PDFs into a single file
 Split a PDF into specific page ranges
 Add watermark PDF pages to an existing PDF
 Lightweight and easy to use

 Installation
bash
Copy
Edit
python -m venv venv
# Activate it:
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
 Usage
 Merge PDFs
Combine multiple PDF files into a single PDF.

bash
Copy
Edit
python main.py merge file1.pdf file2.pdf -o combined.pdf
file1.pdf file2.pdf = PDF files to merge

-o combined.pdf = (optional) name of the output file. Default: merged.pdf

 Split PDF
Extract a specific page range from a PDF.

bash
Copy
Edit
python main.py split input.pdf 2-5
input.pdf = the source PDF

2-5 = page range (inclusive)

Output file will be split_2-5.pdf

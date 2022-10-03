# file: pdf_to_json.py

#only works with python2!
# usage:
#     python3 pdf_to_json.py

# https://pypi.org/project/PyPDF2/
# https://pypdf2.readthedocs.io/en/latest/index.html
# https://github.com/py-pdf/PyPDF2

import PyPDF2
from PyPDF2 import PdfReader

path_to_example_pdf = "../data/infiles/19960012161.pdf"

reader = PdfReader( path_to_example_pdf )
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)
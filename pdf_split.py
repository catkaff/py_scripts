#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyPDF2 import PdfWriter, PdfReader

def pdf_split(fname, start, end=None):
    print('pdf_split', fname, start, end)

    inputpdf = PdfReader(open(fname, "rb"))
    output = PdfWriter()

    num_pages = len(inputpdf.pages)
    if start:
        start -= 1
    if not start:
        start = 0
    if not end or end > num_pages:
        end = num_pages

    get_pages = list(range(start, end))
    print(f'GET pages: {get_pages}')

    for i in range(start, end):
        if i < start:
            continue
        output.add_page(inputpdf.pages[i])

    fname_no_pdf = fname
    if fname[-4:].lower() == '.pdf':
        fname_no_pdf = fname[:-4]
    out_filename = f"{fname_no_pdf}-{start+1}-{end}.pdf"
    with open(out_filename, "wb") as outputStream:
        output.write(outputStream)
    print('saved', out_filename)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python script_name.py path_to_pdf start_page [end_page]")
        sys.exit(1)

    path_to_pdf = sys.argv[1]
    start_page = int(sys.argv[2])

    if len(sys.argv) == 4:
        end_page = int(sys.argv[3])
        pdf_split(path_to_pdf, start_page, end_page)
    else:
        pdf_split(path_to_pdf, start_page)

#./pdf_split.py elk8.pdf 24 48 
#saved elk8-24-48.pdf

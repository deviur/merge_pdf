#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

"""

from PyPDF2 import PdfFileMerger
import os


def get_pdf_files():
    return [file for file in os.listdir() if file.endswith('.pdf')]


def load_pdf_files():
    with open('content_pdf.txt', 'r') as fp:
        return [line.rstrip() for line in fp.readlines()]


def main():

    if os.path.isfile('merged.pdf'):
        os.remove('merged.pdf')

    try:
        open('content_pdf.txt', 'r')
    except FileNotFoundError:
        with open('content_pdf.txt', 'w') as fp:
            for f in get_pdf_files():
                fp.write(f + '\n')
        return

    pdfs = PdfFileMerger()
    for pdf in load_pdf_files():
        pdfs.append(open(pdf, 'rb'))

    with open('merged.pdf', 'wb') as merged_pdf:
        pdfs.write(merged_pdf)


if __name__ == '__main__':
    main()

# merge_pdf
CLI utility to merge some pdf files in one.

Merge pdf files in the current directory.

The first run creates a file with a list of pdf files 'content_pdf.txt' to sort or delete unnecessary.

The second run creates a merged pdf file based on the list from  'content_pdf.txt'.

## Install:
```
pip install -r requirements.txt
```

## Usage:
```
python3 merge_pdf.py
```
The first run creates a text file “content_pdf.txt” with a list of pdf files in the current directory. This list can be sorted in the order in which the pdf files need to be merged.

The second run merges all pdf files listed in “content_pdf.txt” into a single pdf file “merged.pdf”

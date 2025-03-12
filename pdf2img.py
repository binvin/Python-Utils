"""
File name: pdf2img.py
Author: Bindu R
Version: 2.0
Description: A simple Python script to convert pdf pages to images.
"""
import argparse
import sys
import os
from pdf2image import convert_from_path

parser = argparse.ArgumentParser(description="A python script to convert pdf to image.")
parser.add_argument("-f", "--filename", help="Full Path to the input pdf with file name.")
parser.add_argument("-t", "--filetype", help="Output file type - JPEG or PNG.")

args = parser.parse_args()

if args.filename and os.path.isfile(args.filename):
    print(f"Filename: {args.filename}")
else :
    print("No input file or Input file doesnt exist! Quitting!")
    sys.exit()

fileExtn = 'jpg'
if args.filetype:
    if args.filetype.lower() == "png":
        fileExtn = 'png'
        print(f"Output file format: {args.filetype}")
    elif args.filetype.lower() == "jpeg":
        print(f"Output file format: {args.filetype}")        
    else :
        args.filetype = "JPEG"
        print("Invalid file format. Using default file format : JPEG.")
else:
    args.filetype = "JPEG"
    print("Using default output format JPEG.")
    
# Convert PDF to images
pages = convert_from_path(args.filename, dpi=100)

# Save each page as an image
for i, page in enumerate(pages):
    # page.save(f'page_{i+1}.png', 'PNG')
    page.save(f'page_{i + 1}.' + fileExtn, args.filetype.upper())  # Change format to 'JPEG'

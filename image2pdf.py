"""
File name: image2pdf.py
Author: Bindu R
Version: 2.0
Description: A simple Python script to convert jpg images to pdf file.
"""
import argparse
import sys
import img2pdf
import os

parser = argparse.ArgumentParser(description="A python script to convert image(s) to pdf.")
parser.add_argument("-f", "--folderpath", help="Full Path to the folder containing image(s).")
parser.add_argument("-o", "--outfile", default='output', help="Name of the Output file without .pdf. Default value is output.")

args = parser.parse_args()

if args.folderpath and os.path.isdir(args.folderpath):
    print(f"Image directory: {args.folderpath}")
else :
    print("No image directory or Image directory doesnt exist! Quitting!")
    sys.exit()
    
# Specify the folder containing the images
image_folder = args.folderpath 

# Get a list of image files and sort them numerically
images = sorted(
    [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(".jpg")],
    # Extract and sort by page number
    key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[1])
)

# Create the PDF
with open(args.outfile + ".pdf", "wb") as f:
    f.write(img2pdf.convert(images))

print(f"PDF created successfully")

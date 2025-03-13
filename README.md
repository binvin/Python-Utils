# 1. pdf2img.py - A simple Python script to convert pdf pages to images.
This script helps you to convert all the pages of a pdf file into jpg or png images.  
  
To use, run  
***pdf2img.py -f full path to the pdf file -t image format JPEG or PNG***  
### Note:  
-t is optional and by default the script creates the images in jpg format.  
The output images are saved in the directory where this script exists.  
  
## Requirements:  
You need to install pdf2image module using "***pip install pdf2image***" command.  

# 2. image2pdf.py - A simple Python script to convert jpg image(s) to pdf.
This script helps you to convert images to a pdf file.  
  
To use, run  
***image2pdf.py -f full path to the fodler containing the images -o output file name, default name is output.***  
### Note:  
-o is optional and by default the script creates a pdf named output.pdf.  
Do not add .pdf to your outputfile name (-o )  
The output pdf is created in the directory where this script exists.  
  
## Requirements:  
You need to install img2pdf module using "***pip install img2pdf***" command.  
  

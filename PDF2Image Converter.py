from tkinter import filedialog
from pdf2image import convert_from_path
from pathlib import Path
import os
pages = filedialog.askopenfilename(title='Please select 1 pdf.',
                                filetypes=[('PDF Files', ['.pdf']),
                                           ('All Files', ['*.*'])])

directory = "Pdf2Image_Files"
myFile = Path(pages).stem
parent_dir = os.getcwd()
path=os.path.join(parent_dir, directory)
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)
with open(pages) as file:
    print(file.name)
    images = convert_from_path(pdf_path=file.name, poppler_path = r"C:\\Users\\sabrs\\anaconda3\\Library\\poppler-0.68.0_x86\\poppler-0.68.0\\bin")
    for i in range(0,len(images)):
        images[i].save(myFile+'_'+str(i) + '.jpg', 'JPEG')


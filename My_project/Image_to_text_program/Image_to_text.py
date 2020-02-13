from PIL import Image
from pytesseract import *
import re
import cv2

img = Image.open('./asdf.jpg')

text = pytesseract.image_to_string(img, lang='chi_sim')

size_table = re.split('\n', text)

print(size_table)
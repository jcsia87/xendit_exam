#ignore this file

import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
im = Image.open(r'C:\Users\Jefferson\Desktop\xendit_exam\tests\image.png') 
# width, height = im.size
# left = 40
# top = 40
# right = 560
# bottom = 120
# im1 = im.crop((left, top, right, bottom))
# im1.show()
# im.show()
print(pytesseract.image_to_string(im, lang='eng',
                    config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'))
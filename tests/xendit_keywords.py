from robot.libraries.BuiltIn import BuiltIn
import pytesseract
from PIL import Image
import io
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class xendit_keywords(object):
    def __init__(self):
        self.seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')

    def sum_should_be(self, sum):
        driver = self.seleniumlib.driver
        image = driver.find_element_by_id("canvas").screenshot_as_png
        cropped_img = self.crop(image)
        # cropped_img.show()
        ocr = pytesseract.image_to_string(cropped_img, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(ocr)
        BuiltIn().should_be_equal(int(sum), int(ocr))

    def difference_should_be(self, diff):
        driver = self.seleniumlib.driver
        image = driver.find_element_by_id("canvas").screenshot_as_png
        cropped_img = self.crop(image)
        # cropped_img.show()
        ocr = pytesseract.image_to_string(cropped_img, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(ocr)
        BuiltIn().should_be_equal(int(diff), int(ocr))

    def quotient_should_be(self, quo):
        driver = self.seleniumlib.driver
        image = driver.find_element_by_id("canvas").screenshot_as_png
        cropped_img = self.crop(image)
        # cropped_img.show()
        ocr = pytesseract.image_to_string(cropped_img, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(ocr)
        BuiltIn().should_be_equal(int(quo), int(ocr))

    def crop(self, image):
        img = Image.open(io.BytesIO(image))
        left = 40
        top = 40
        right = 530
        bottom = 115
        img2 = img.crop((left, top, right, bottom))
        return img2

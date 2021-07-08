import cv2
import pytesseract
from pathlib import Path


class ORCImages():
    def __init__(self, file):
        self.file = file
        # Подключение фото
        img = cv2.imread(self.file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Будет выведен весь текст с картинки
        config = r'--oem 3 --psm 6'
        self.text = pytesseract.image_to_string(img, config=config, lang='rus')

if __name__ == '__main__':
    # Путь для подключения tesseract
    # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    BASE_DIR = Path(__file__).resolve().parent.parent
    files = str(BASE_DIR)+'/Scripts/test.jpg'

    testclassORC = ORCImages(files)

    print(testclassORC.text)
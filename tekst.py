


import cv2
import pytesseract
import numpy as np

# Wczytanie obrazu z pliku
img = cv2.imread('/Users/przemo/Downloads/hybryda.jpg')

# Przeprowadzenie wstępnego przetwarzania obrazu
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 20, 20, 20)
edged = cv2.Canny(gray, 50, 220)

# Znalezienie konturów na obrazie
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

# Znalezienie prostokąta obejmującego tablicę rejestracyjną
screenCnt = None
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break

# Wycięcie i przekształcenie obrazu tablicy rejestracyjnej
if screenCnt is not None:
    mask = np.zeros(gray.shape, np.uint8)
    new_img = cv2.drawContours(mask, [screenCnt], 0, 255, -1)
    new_img = cv2.bitwise_and(img, img, mask = mask)
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    cropped = gray[topx:bottomx+1, topy:bottomy+1]

    # Rozpoznanie tekstu na tablicy rejestracyjnej
    text = pytesseract.image_to_string(cropped, lang='pol')
    print("Numer rejestracyjny to:", text)
else:
    print("Nie znaleziono tablicy rejestracyjnej na obrazie.")
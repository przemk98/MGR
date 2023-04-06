import cv2
import numpy as np

# Wczytanie obrazu
img = cv2.imread('/Users/przemo/Downloads/gwiazda_poranna.png')

# Konwersja obrazu do skali szarości
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Zastosowanie binaryzacji
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Wykrycie konturów
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Przeszukanie konturów w poszukiwaniu formacji "gwiazdy porannej"
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y+h, x:x+w]
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, roi_thresh = cv2.threshold(roi_gray, 127, 255, cv2.THRESH_BINARY)
        _, roi_contours = cv2.findContours(roi_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(roi_contours) == 3:
            print("Wykryto formację 'gwiazdy porannej' na wykresie.")
        else:
            print("Tu nie ma formacji gwiazdy")
import cv2
import numpy as np

# Wczytanie obrazu wykresu świecowego
img = cv2.imread('wykres.png')

# Konwersja obrazu na odcienie szarości
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Zastosowanie progowania adaptacyjnego
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

# Wykrycie konturów na obrazie
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iteracja po konturach
for i, contour in enumerate(contours):
    # Aproksymacja konturu
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    # Sprawdzenie, czy kontur ma odpowiedni kształt formacji analizy technicznej
    if len(approx) == 3:
        print("Wykryto trójkąt - możliwa formacja Spadającej Gwiazdy")
    elif len(approx) == 4:
        print("Wykryto czworokąt - możliwa formacja Młotka lub Wiszącego Człowieka")
    elif len(approx) == 5:
        print("Wykryto pięciokąt - możliwa formacja Diamentu")
    elif len(approx) == 6:
        print("Wykryto sześciokąt - możliwa formacja Głowy i Ramion")
    elif len(approx) > 6:
        print("Wykryto wielokąt - możliwa formacja Trójkąta")
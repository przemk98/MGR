import cv2
import numpy as np
#talib.py
import talib
# Wczytanie obrazu wykresu
img = cv2.imread('wykres.png')

# Konwersja na odcienie szarości
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Wykrywanie formacji
wedges, _, _, _ = talib.CDLRISEFALL3METHODS(gray)
hns, _, _, _ = talib.CDLINVERTEDHAMMER(gray)
flags, _, _, _ = talib.CDLFLAG(gray)
pennants, _, _, _ = talib.CDLPENNT(gray)

# Wyświetlanie wyników
if wedges[-1] != 0:
    print("Wykryto formację klina na wykresie")
if hns[-1] != 0:
    print("Wykryto formację głowy i ramion na wykresie")
if flags[-1] != 0:
    print("Wykryto formację flagi na wykresie")
if pennants[-1] != 0:
    print("Wykryto formację chorągiewki na wykresie")

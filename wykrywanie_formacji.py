import cv2
import numpy as np

# Wczytanie obrazu
img = cv2.imread('wykres.png', 0)

# Wykrywanie krawędzi z użyciem Canny
edges = cv2.Canny(img, 100, 200)

# Wykrywanie konturów
contours=  cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Wykrywanie formacji analizy technicznej
for cnt in contours:
    # Liczenie liczby wierzchołków w konturze
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    vertices = len(approx)

    # Wykrywanie formacji podwójne szczyty i dno
    if vertices == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y+h, x:x+w]

        # Obliczenie wartości średniej dla regionu zainteresowania
        mean_val = cv2.mean(roi)

        # Analiza wyników dla formacji podwójne szczyty i dno
        if mean_val < 100:
            print("Formacja podwójne szczyty")
        elif mean_val > 150:
            print("Formacja podwójne dno")
        else:
            print("Brak formacji")

# Wyświetlenie wyników
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
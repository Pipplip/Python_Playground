'''
Webcam nutzen

Voraussetzung:
pip install opencv-python numpy matplotlib
'''
import cv2

cam = cv2.VideoCapture(0)

while True:
    _, image = cam.read() # Kamera lesen (read liefert 2 Values, wir brauchen aber nur image)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # schwarz-weiß Bild
    edges = cv2.Canny(gray, 30, 100) # Kantenbild mit Canny Algorithmus
    
    # Kamera Screens anzeigen
    cv2.imshow("LiveVideo", image)
    #cv2.imshow("Gray scale", gray)
    cv2.imshow("Edgesscale", edges)

    if cv2.waitKey(1) == ord("q"): # Wenn q gedrückt wird, wird Programm geschlossen
        break

# nachdem q gedrückt wurde -> cv ordentlich schliessen
cam.release()
cv2.destroyAllWindows()

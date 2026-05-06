import cv2
import numpy as np
from deepface import DeepFace

class FaceEngine:
    def __init__(self):
        self.modelo = "Facenet"  # Modelo que convierte la cara en un vector

    def detectar_cara(self, frame):
        """
        Detecta si hay una cara en la imagen.
        Devuelve True/False y las coordenadas del rostro.
        """
        detector = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        caras = detector.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

        if len(caras) > 0:
            return True, caras[0]  # Devuelve la primera cara encontrada
        return False, None

    def obtener_vector(self, imagen_path):
        """
        Convierte una imagen de cara en un vector numérico (embedding).
        Esto es lo que permite comparar dos rostros matemáticamente.
        """
        try:
            resultado = DeepFace.represent(
                img_path=imagen_path,
                model_name=self.modelo,
                enforce_detection=False
            )
            vector = np.array(resultado[0]["embedding"])
            return vector
        except Exception as e:
            print(f"Error al obtener vector: {e}")
            return None

    def dibujar_cuadricula(self, frame, cara_coords):
        """
        Dibuja la cuadrícula (como el 3 en raya) sobre la cara detectada.
        Divide la cara en 9 zonas para análisis por regiones.
        """
        x, y, w, h = cara_coords

        # Dibuja el rectángulo principal alrededor de la cara
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Divide en 3 columnas y 3 filas (cuadrícula 3x3)
        tercio_w = w // 3
        tercio_h = h // 3

        for i in range(1, 3):
            # Líneas verticales
            cv2.line(frame, (x + tercio_w * i, y), (x + tercio_w * i, y + h), (0, 255, 0), 1)
            # Líneas horizontales
            cv2.line(frame, (x, y + tercio_h * i), (x + w, y + tercio_h * i), (0, 255, 0), 1)

        return frame
import cv2

class Camera:
    def __init__(self):
        self.captura = None

    def iniciar(self):
        """Abre la cámara del computador"""
        self.captura = cv2.VideoCapture(0)
        return self.captura.isOpened()

    def obtener_frame(self):
        """Devuelve un frame (imagen) de la cámara"""
        if self.captura and self.captura.isOpened():
            ret, frame = self.captura.read()
            if ret:
                return frame
        return None

    def tomar_foto(self):
        """Captura una sola foto y la devuelve"""
        frame = self.obtener_frame()
        return frame

    def detener(self):
        """Cierra la cámara"""
        if self.captura:
            self.captura.release()
        cv2.destroyAllWindows()
from core.camera import Camera
from core.face_engine import FaceEngine
import cv2

cam = Camera()
engine = FaceEngine()

if cam.iniciar():
    print("Cámara iniciada - Presiona 'q' para salir")
    while True:
        frame = cam.obtener_frame()
        if frame is not None:
            hay_cara, coords = engine.detectar_cara(frame)
            if hay_cara:
                frame = engine.dibujar_cuadricula(frame, coords)
            cv2.imshow("Scanner Facial", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.detener()
else:
    print("No se pudo abrir la cámara")
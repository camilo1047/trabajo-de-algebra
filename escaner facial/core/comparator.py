import numpy as np

class Comparator:
    def __init__(self, umbral=0.5):
        """
        umbral: porcentaje mínimo de similitud para dar acceso (0.5 = 50%)
        """
        self.umbral = umbral

    def calcular_similitud(self, vector1, vector2):
        """
        Compara dos vectores faciales usando similitud coseno.
        Devuelve un valor entre 0 y 1 (0% a 100% de similitud).
        
        Esto es álgebra lineal pura:
        similitud = (v1 · v2) / (||v1|| * ||v2||)
        """
        vector1 = np.array(vector1)
        vector2 = np.array(vector2)

        producto_punto = np.dot(vector1, vector2)
        norma1 = np.linalg.norm(vector1)
        norma2 = np.linalg.norm(vector2)

        if norma1 == 0 or norma2 == 0:
            return 0.0

        similitud = producto_punto / (norma1 * norma2)
        # Convertir a rango 0-1
        similitud = (similitud + 1) / 2
        return round(float(similitud), 4)

    def verificar_acceso(self, vector_guardado, vector_actual):
        """
        Compara la cara guardada con la cara actual.
        Devuelve True si la similitud supera el umbral.
        """
        similitud = self.calcular_similitud(vector_guardado, vector_actual)
        porcentaje = similitud * 100
        print(f"Similitud: {porcentaje:.1f}%")

        if similitud >= self.umbral:
            print("✅ Acceso concedido")
            return True, porcentaje
        else:
            print("❌ Acceso denegado")
            return False, porcentaje
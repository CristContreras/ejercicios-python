class Vehiculo:
    def __init__(self, nombre: str, velocidad_maxima: int):
        self.__nombre = nombre
        self.__velocidad_maxima = velocidad_maxima
        self.__distancia_recorrida = 0

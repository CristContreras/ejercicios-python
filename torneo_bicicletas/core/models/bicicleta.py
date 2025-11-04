from .vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, nombre: str, velocidad_maxima: int, resistencia: int):
        super().__init__(nombre, velocidad_maxima)
        self.__resistencia: int = resistencia
    
    def avanzar(self):
        pass

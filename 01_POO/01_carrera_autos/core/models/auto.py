import random as r

class Auto:
    def __init__(self,nombre:str, velocidad_maxima:int):
        self.__nombre=nombre
        self.__velocidad_maxima = velocidad_maxima
        self.__posicion_actual=0

    
    @property #getter
    def nombre(self)->str:
        return self.__nombre

    @property #getter
    def velocidad_maxima(self):
        return self.__velocidad_maxima
    
    @property
    def posicion_actual(self):
        return self.__posicion_actual

    #region métodos
    def avanzar(self) -> None:
        metros = r.randint(10, self.__velocidad_maxima)
        self.__posicion_actual+=metros
    
    def obtener_estado(self) -> str:
        return f"Nombre {self.__nombre} - Posición: {self.__posicion_actual}"
    #endregion

#explicacion
"""En la vida real, un auto rápido siempre va más rápido que uno lento en el mismo tiempo.

En la simulación, cada turno es como lanzar un dado: el máximo del dado depende de la velocidad,
 pero el resultado puede ser menor.

Por eso nuestra intuición falla: esperamos que el auto rápido siempre esté adelante, 
pero la aleatoriedad puede cambiar el orden momentáneamente."""
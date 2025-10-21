from .auto import Auto

class Carrera:
    def __init__(self):
        self.__autos: list[Auto]=[]
        self.__turno=5
    
    def agregar_auto(self, Auto)->None:
        self.__autos.append(Auto)

    def iniciar_carrera(self) -> list[str]:
        estados: list[str]=[]
        for i in range(self.__turno):
            #print(f"Turno {i+1}")
            for auto in self.__autos:
                auto.avanzar()
                estados.append(auto.obtener_estado())
        return estados

    def mostrar_progreso(self):
        pass

    def obtener_ganador(self) -> int | list[int]:
        indices: list[int] = []
        #1. obtener el mayor
        mayor = 0
        indice = 0
        for i in range(len(self.__autos)):
            if self.__autos[i].posicion_actual > mayor:
                mayor = self.__autos[i].posicion_actual
                indice = i
        
        #guarda en primera posicion despues de salir del for
        indices.append(indice)

        #2.verifica empate
        for i in range(len(self.__autos)):
            if self.__autos[i].posicion_actual == mayor:
                for indice in indices:
                    if i != indice:
                        indices.append(i)
        
        return mayor, indices
        
        







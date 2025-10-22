from .auto import Auto

class Carrera:
    def __init__(self):
        self.__autos: list[Auto] = []
        self.__turno: int = 5

    def obtener_turno(self):
        return self.__turno
    
    def agregar_auto(self, Auto)->None:
        self.__autos.append(Auto)

    def obtener_autos(self)->list[Auto]:
        return self.__autos
 
    def iniciar_carrera(self) -> list[str]:
        turnos: list[list[str]] = []
        for i in range(self.__turno):
            turno_actual = [] # se reincia la lista
            for auto in self.__autos:
                auto.avanzar() #avanza 1 turno
                estado = auto.obtener_estado()
                turno_actual.append(estado)
            turnos.append(turno_actual)
        return turnos

    def obtener_ganador(self) ->list[int]:
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
        #return [auto.obtener_estado() for auto in self.__autos]
        return indices






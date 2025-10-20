from auto import Auto

class Carrera:
    def __init__(self):
        self.__autos: list[Auto]=[]
        self.__turno=5
    
    def agregar_auto(self, Auto)->None:
        self.__autos.append(Auto)

    def iniciar_carrera(self):
        for i in range(self.__turno):
            print(f"Turno {i+1}")
            for auto in self.__autos:
                auto.avanzar()
                auto.mostrar_estado()
    
    def mostrar_progreso(self):
        pass

    def mostrar_ganador(self):
        #cada auto tiene una posicion en metros
        
        #sacar el mayor a una variabel
        #buscar en el original otro igual
        #mayor:Auto = None

        lista_velocidades: list[Auto]=[]
        lista_ganadores=list[int]=[]

        repetir = True
        for auto in self.__autos: #guardo las posiciones
            lista_velocidades.append(auto.posicion_actual)
        
        mayor = lista_velocidades[0]
        indice: int

        mayor = max(lista_velocidades.pop())
        for i in range(len(lista_velocidades)):
            if mayor < lista_velocidades[i]:
                mayor = lista_velocidades[i]
                indice = i

        del lista_velocidades[indice]


        








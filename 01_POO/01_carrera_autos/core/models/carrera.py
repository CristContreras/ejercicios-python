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

        velocidades: list[Auto]=self._obtener_velocidades()
        lista_auxiliar: list[dict]=[]
        

    def _obtener_velocidades(self):
        return [auto.posicion_actual for auto in self.__autos]
    
    def _obtener_maximos(self, lista_velocidades:list):
        repetir = True
        empate = False
        mayor = 0
        while repetir:
            for i in range(len(lista_velocidades)):
                if lista_velocidades[i]>mayor:
                    mayor=lista_velocidades[i]
            
    def _obtener_ganador(self, velocidades):
        mayor = 0
        empate = False
        indice =0

        for i in range(len(velocidades)): #ver si cada elemento es mayor
            if velocidades[i]>mayor:
                mayor=velocidades[i]
                indice = i
                
            if velocidades[i]==mayor:
                empate=True

        



    #[12,34,56,12]
    #lista ganadores: [{"Inidice": 0, "velocidad": 12},{"indice":0}]








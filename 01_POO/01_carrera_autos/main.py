from core.models.auto import Auto
from core.models.carrera import Carrera

def main():
    auto1 = Auto("Rayo", 200)
    auto2 = Auto("Cris", 120)
    auto3 = Auto("Carlos", 100)

    carrera = Carrera()

    carrera.agregar_auto(auto1)
    carrera.agregar_auto(auto2)
    carrera.agregar_auto(auto3)

    turnos = carrera.iniciar_carrera()
    for i, turno in enumerate(turnos, start=1):
         print(f"Turno {i}")
         for estado in turno:
              print(estado)
         print()
    
    ganadores = carrera.obtener_ganador()
    ganador = ganadores[0]
    lista = carrera.obtener_autos()
    print(lista[ganador].nombre)
    print(lista[ganador].posicion_actual)
   # mostrar_progreso(estados)
    
    #print(*(carrera.obtener_progreso(estados)), end="\n")
    #recorrer los estados despues

  
def mostrar_progreso(estados: list[str]):
        for estado in estados:
             print(estado)

if __name__=="__main__":
    main() 
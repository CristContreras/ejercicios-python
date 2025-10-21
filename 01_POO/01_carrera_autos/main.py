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

    estados = carrera.iniciar_carrera()
    #recorrer los estados despues

if __name__=="__main__":
    main() 
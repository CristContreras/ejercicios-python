import random

class Robot:
    def __init__(self, nombre: str):
        self.__nombre: str=nombre
        self.__energia=100
        self.__ataque = random.randint(1,100)
        self.__defensa = random.randint(1,100)
    
    def atacar_robot(self, robot: "Robot"):
        #el ataque se reduce por la defensa, y ese resultado le resta a energia
        danio_total = robot.__defensa - self.__ataque
        robot.recibir_golpe(danio_total)

    def recibir_golpe(self, danio: int):
        self.__energia -= danio
    
    
    def obtener_estado(self):
        
    #que sea aleatorio el ataque y defensa
    def __str__(self):
        pass
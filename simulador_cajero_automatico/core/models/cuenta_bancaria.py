class Cuenta_bancaria:
    def __init__(self, saldo: float, titular: str):
        self.__saldo: float=saldo
        self.__titular: str=titular
    
    def depositar(self, monto: float):
        self.__saldo+=monto
        #Solicita ingreso de monto? NO
        #Controla q sea mayor a cero
        #Debe controlar q sea float?
        #Debe indicar con print q se deposito con exito?
        #Si solo hace el diposito como indica su nombre, esta bien? 
        #Entonces hace de hacer un deposito tendria q controlar q el tipo de dato es correcto
        #Resultado: programa más dividido
        
    #donde va los controles y validaciones para el ingreso ? 
    #debe ir del lado de la clase ?

        
    def retirar(self, monto: float):
        self.__saldo-=monto
    
    def fue_retirado(self):
        pass
    
    def es_monto_valido(self):
        pass

    @property
    def saldo(self):
        return self.__saldo
    
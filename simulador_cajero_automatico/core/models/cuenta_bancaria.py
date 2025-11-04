class Cuenta_bancaria:
    def __init__(self, saldo: float, titular: str):
        self.__saldo: float=saldo
        self.__titular: str=titular

    def _validar_monto(self, monto: float):
        if monto <= 0:
            raise ValueError("Error no puede ser cero")

    def depositar(self, monto: float):
        self._validar_monto(monto)
        self.__saldo+=monto

    def retirar(self, monto: float):
        if monto > 0 and monto < self.__saldo:
            self.__saldo-=monto
        else:
            raise ValueError("El monto debe ser menor al saldo disponible y mayor a cero")
    def fue_retirado(self):
        pass
    
    def es_monto_valido(self):
        pass

    @property
    def saldo(self):
        return self.__saldo
    
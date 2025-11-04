from core.models.cuenta_bancaria import Cuenta_bancaria

def obtener_monto():
    repetir=True
    while repetir:
        try:
            monto = float(input("Ingrese monto"))
            repetir=False
            return monto
        except ValueError as e:
            print(f"Error de conversion, debe ingresar solo numeros - {e}")

def procesar_deposito(cuenta: Cuenta_bancaria):
    repeat_deposito = True
    while repeat_deposito:
        monto = obtener_monto()
        try:
            cuenta.depositar(monto)
            repeat_deposito=False
        except ValueError as e:
            print(e)

def procesar_retiro(cuenta: Cuenta_bancaria):
    repeat_retiro=True
    while repeat_retiro:
        monto = obtener_monto()
        try:
            cuenta.retirar(monto)
            print(f"Retiro de ${monto} exitoso")
            print(f"Saldo actual ${cuenta.saldo}")
            repeat_retiro=False
        except ValueError as e:
            print(e)
def generar_cuenta(saldo: float, titular: str):
    return Cuenta_bancaria(saldo, titular)

def main():
    cuenta=generar_cuenta(200, "Juan")
    procesar_deposito(cuenta)
    procesar_retiro(cuenta)

    

if __name__=="__main__":
    main()



        








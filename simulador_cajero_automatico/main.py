from core.models.cuenta_bancaria import Cuenta_bancaria

def main():
    cuenta = Cuenta_bancaria(200, "Juan")
    repetir = True
    opcion = input("Ingrese una opcion")
    match(opcion):
        case "1":
            pass
        
if __name__=="__main__":
    main()

def es_monto_valido(monto: str):
    try:
        monto = float(monto)
        return True
    except ValueError as e:
        return False, e

def procesar_deposito(cuenta: Cuenta_bancaria):
    repetir = True
    while repetir:
        monto = input("Ingrese monto a depositar: ")
        if es_monto_valido(monto):
            cuenta.depositar(monto)
        else:








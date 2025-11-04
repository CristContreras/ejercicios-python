from core.models.cuenta_bancaria import Cuenta_bancaria

def obtener_monto(mensaje):
    repetir=True
    while repetir:
        try:
            monto = float(input(mensaje))
            repetir=False
            return monto
        except ValueError as e:
            print(f"Error de conversion, debe ingresar solo numeros - {e}")

def procesar_deposito(cuenta: Cuenta_bancaria):
    repeat_deposito = True
    while repeat_deposito:
        monto = obtener_monto("Ingrese monto de deposito: $")
        try:
            cuenta.depositar(monto)
            repeat_deposito=False
        except ValueError as e:
            print(e)

def procesar_retiro(cuenta: Cuenta_bancaria):
    repeat_retiro=True
    while repeat_retiro:
        monto = obtener_monto("Ingrese monto de retiro: $")
        try:
            cuenta.retirar(monto)
            print(f"Retiro de ${monto} exitoso")
            print(f"Saldo actual ${cuenta.saldo}")
            repeat_retiro=False
        except ValueError as e:
            print(e)

def generar_cuenta(saldo: float, titular: str):
    return Cuenta_bancaria(saldo, titular)

def mostrar_opciones():
    print("1. Depositar\n" \
    "2. Retirar\n" \
    "3. Salir")

def procesar_opcion(opcion: str, cuenta: Cuenta_bancaria):
    match(opcion):
        case 1:
            procesar_deposito(cuenta)
        case 2:
            pass
        case 3:
            sys.exit()
        case _:
            print("Opcion incorrecta")
            sys.exit()

import sys
import os
import time

def limpiar_pantalla():
    os.system("cls")

def mostrar_saldo(cuenta: Cuenta_bancaria):
    print(f"Saldo disponible ${cuenta.saldo}")

def ejecutar_menu(cuenta: Cuenta_bancaria):
    repetir = True
    while repetir:
        mostrar_saldo(cuenta)
        print()
        mostrar_opciones()
        print()
        try:
            opcion=int(input("Ingrese una opción: "))
            procesar_opcion(opcion, cuenta)
        except ValueError as e:
            print()
            print("❌ Error debe ingresar un numero.")
            time.sleep(2)
            os.system("cls")

def main():
    cuenta=generar_cuenta(200, "Juan")
    ejecutar_menu(cuenta)
    


    

if __name__=="__main__":
    main()



        








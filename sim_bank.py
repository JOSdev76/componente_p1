import json
import os
import time

ARCHIVO = "banco.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as file:
            json.dump({"usuarios": {}}, file, indent=4)
    with open(ARCHIVO, "r") as file:
        return json.load(file)

def guardar_datos(data):
    with open(ARCHIVO, "w") as file:
        json.dump(data, file, indent=4)

def registrar_usuario():
    data = cargar_datos()
    usuarios = data["usuarios"]

    usuario = input("Crea un nombre de usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe.")
        return None

    contraseña = input("Crea una contraseña: ")
    usuarios[usuario] = {"password": contraseña, "saldo": 0}
    guardar_datos(data)
    print("Usuario creado con éxito.")
    return usuario

def iniciar_sesion():
    data = cargar_datos()
    usuarios = data["usuarios"]

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        print(f"Bienvenido {usuario}")
        return usuario
    else:
        print("Credenciales incorrectas")
        return None


def menu(usuario):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"=== BANCO VIRTUAL ===\nUsuario: {usuario}")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        data = cargar_datos()
        saldo = data["usuarios"][usuario]["saldo"]

        if opcion == "1":
            print(f"\nTu saldo actual es: {saldo}")
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            try:
                monto = float(input("Monto a depositar: "))
                if monto > 0:
                    data["usuarios"][usuario]["saldo"] += monto
                    guardar_datos(data)
                    print(f"Depósito exitoso. Nuevo saldo: {data['usuarios'][usuario]['saldo']}")
                else:
                    print("El monto debe ser mayor a 0.")
            except ValueError:
                print("Ingresa un número válido.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":  # Retirar
            try:
                monto = float(input("Monto a retirar: "))
                if monto <= 0:
                    print("El monto debe ser mayor a 0.")
                elif monto <= saldo:
                    data["usuarios"][usuario]["saldo"] -= monto
                    guardar_datos(data)
                    print(f"Retiro exitoso. Nuevo saldo: {data['usuarios'][usuario]['saldo']}")
                else:
                    print("Saldo insuficiente.")
            except ValueError:
                print("Ingresa un número válido.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            print("Cerrando sesión...")
            time.sleep(1)
            break
        else:
            print("Opción inválida.")
            time.sleep(1)

#login seria la primera parte
while True:
    os.system("cls" if os.name == "nt" else "clear") #para usarlo en win o linux (pydorid)
    print("=== PLATAFORMA BANCARIA ===")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        usuario = iniciar_sesion()
        if usuario:
            menu(usuario)

    elif opcion == "2":
        registrar_usuario()

    elif opcion == "3":
        print("Gracias por usar el banco. ¡Adiós!")
        break
    else:
        print("Opción inválida.")
        time.sleep(1)

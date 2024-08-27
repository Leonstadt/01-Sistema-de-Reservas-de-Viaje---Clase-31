#sistema de reserva practica de examen
from datetime import datetime
usuarios=[]
reservas=[]
def menu():
    #mostrar el menu principal
    while True:
        print("Menu Principal")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar una reserva")
        print("5. Salir del programa")
        
        opcion=input("Seleccione una opcion: ")
        
        if opcion =='1':
            registrar_usuario()
            
        elif opcion == '2':
            reservar_viaje()
        elif opcion == '3':
            ver_reservas()
        elif opcion == '4':
            cancelar_reserva()
        elif opcion == '5':
            print("Gracias por usar el sistema")
            break
        else:
            print("Opcion invalida, Por favor intente otra vez")
            
def registrar_usuario():
    #nos permite ingresar el usuario
    while True:
        nombre=input("Ingrese el nombre del Usuario: ").strip().lower()
        if nombre:
            if nombre in usuarios:
               print(f"El Usuario {nombre} ya existe, intentelo con otro Usuario.")     
            else:
                usuarios.append(nombre)   
                print(f"Usuario {nombre} agregado")
                break
        else:
            print("El campo no puede estar vacio")   
                       
def reservar_viaje():
    #nos permite agregar el registro de viaje al usuario
    nombre=input("Ingrese el Usuario que va a reservar el viaje: ").strip().lower()
    if nombre not in usuarios:
        print("Usuario no registrado, Por favor, registrate primero.")
        registrar_usuario()
    
    destino=input(f"Ingrese el destino a reservar, {nombre} ").strip().lower()
    while True:
        fecha=input(f"Ingrese la fecha en la que viajara, {nombre} en formato DD/MM/AAAA: ").strip()
        try:
            validacion_fecha=datetime.strptime(fecha, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha invalida, por favor, intentelo nuevamente en el formato solicitado. ")
    reserva={"nombre": nombre, "destino": destino, "fecha":fecha}
    reservas.append(reserva)
    print(f"La reserva para {nombre} hacia {destino} el {fecha} ha sido realizada")

def ver_reservas():
    #nos deja ver las reservas hechas
    nombre=input("Introduce el Usuario que deseas consultar: ").strip().lower()   
    if nombre in usuarios:
        reservas_usuario=[]
        for reserva in reservas:
            if reserva["nombre"] == nombre:
                reservas_usuario.append(reserva)
        if reservas_usuario:
            print(f"Reservas de {nombre}: ")
            for i, reserva in enumerate(reservas_usuario, 1):
                print(f"{i}. Destino: {reserva["destino"]}, Fecha: {reserva["fecha"]}")
        else:
            print(f"{nombre} no tiene reservas")
    else:
        print("Usuario no encontrado, Por favor, Registrate.")

def cancelar_reserva():
    #nos deja cancelar la reserva del usuario
    nombre=input("Ingresa el nombre del Usuario a cancelar la reserva: ").strip().lower()
    if nombre in usuarios:
        reservas_usuario=[]
        for reserva in reservas:
            if reserva["nombre"] == nombre:
                reservas_usuario.append(reserva)
        if reservas_usuario:
            print(f"Reservas de {nombre}: ")
            for i, reserva in enumerate(reservas_usuario, 1):
                print(f"{i}. Destino: {reserva["destino"]}, Fecha: {reserva["fecha"]}")
            
            seleccion=int(input("Selecciona el numero de la reserva a cancelar: "))
            if 1 <= seleccion <= len(reservas_usuario):
                reservas.remove(reservas_usuario[seleccion-1])
                print("Reserva cancelada con exito")
            else:
                print("Seleccion invalida")
        else:
                print(f"{nombre} no tiene reservas")
    else:
            print("Usuario no econtrado, Por favor, Registrate.")
        

menu()  
 
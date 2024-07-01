import threading


# Función para imprimir la tabla de multiplicar de un número dado
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Crear hilos para las tablas de multiplicar
hilo_1 = threading.Thread(target=tabla_multiplicar, args=(numero,))
hilo_2 = threading.Thread(target=tabla_multiplicar, args=(numero + 1,))

# Iniciar los hilos
hilo_1.start()
hilo_2.start()

# Esperar a que los hilos terminen
hilo_1.join()
hilo_2.join()

print("Las tablas de multiplicar han sido calculadas.")

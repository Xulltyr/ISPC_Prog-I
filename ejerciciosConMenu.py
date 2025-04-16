""""
1. Escribe un programa que tenga un menú para gestionar un inventario de productos:
    a. Agregar Producto
    b. Mostrar Inventario
    c. Buscar Producto
    d. Eliminar Producto
    e. Salir"""
def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    
    inventario[nombre] = {
        'cantidad': cantidad,
        'precio': precio
    }
    print(f"Producto '{nombre}' agregado al inventario.")
def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    
    print("Inventario:")
    for nombre, detalles in inventario.items():
        print(f"{nombre}: {detalles['cantidad']} unidades a ${detalles['precio']} cada una")
def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    
    if nombre in inventario:
        detalles = inventario[nombre]
        print(f"{nombre}: {detalles['cantidad']} unidades a ${detalles['precio']} cada una")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")     
def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")     
def menu_inventario():
    inventario = {}
    
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Buscar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            mostrar_inventario(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            eliminar_producto(inventario)
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intente nuevamente.")
      
menu_inventario()    
    
""". Escribe un programa que tenga un menú para gestionar una lista de contactos.
    a. Agregar Contacto
    b. Eliminar Contacto
    c. Mostrar Contacto
    d. Salir"""
def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado.")
def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")
def mostrar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a mostrar: ")
    
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")
def menu_agenda():
    agenda = {}
    
    while True:
        print("\nMenú de Agenda:")
        print("1. Agregar Contacto")
        print("2. Eliminar Contacto")
        print("3. Mostrar Contacto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            eliminar_contacto(agenda)
        elif opcion == '3':
            mostrar_contacto(agenda)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, intente nuevamente.")
            
menu_agenda()
    
"""3. Escribe un programa que tenga un menú para gestionar los usuarios y password de tus aplicaciones."""
def agregar_usuario(usuarios):
    usuario = input("Ingrese el nombre del usuario: ")
    password = input("Ingrese la contraseña: ")
    
    if usuario in usuarios:
        print(f"El usuario '{usuario}' ya existe.")
    else:
        usuarios[usuario] = password
        print(f"Usuario '{usuario}' agregado.")
def eliminar_usuario(usuarios):
    usuario = input("Ingrese el nombre del usuario a eliminar: ")
    
    if usuario in usuarios:
        del usuarios[usuario]
        print(f"Usuario '{usuario}' eliminado.")
    else:
        print(f"El usuario '{usuario}' no se encuentra registrado.")
def mostrar_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for usuario in usuarios:
            print(f"- {usuario}")
def menu_usuarios():
    usuarios = {}
    
    while True:
        print("\nMenú de Gestión de Usuarios:")
        print("1. Agregar Usuario")
        print("2. Eliminar Usuario")
        print("3. Mostrar Usuarios")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_usuario(usuarios)
        elif opcion == '2':
            eliminar_usuario(usuarios)
        elif opcion == '3':
            mostrar_usuarios(usuarios)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu_usuarios()

"""4. Escribe un programa que tenga un menú para gestionar las tareas que permita agregar, marcar como completadas y 
mostrar tareas pendientes."""
def agregar_tarea(tareas):
    tarea = input("Ingrese la tarea: ")
    tareas.append({'tarea': tarea, 'completada': False})
    print(f"Tarea '{tarea}' agregada.")
def marcar_completada(tareas):
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = True
        print(f"Tarea '{tareas[indice]['tarea']}' marcada como completada.")
    else:
        print("Número de tarea inválido.")
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("Tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea['completada'] else "Pendiente"
        print(f"{i}. {tarea['tarea']} - {estado}")
def menu_tareas():
    tareas = []

    while True:
        print("\nMenú de Gestión de Tareas:")
        print("1. Agregar Tarea")
        print("2. Marcar Tarea como Completada")
        print("3. Mostrar Tareas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            marcar_completada(tareas)
        elif opcion == '3':
            mostrar_tareas(tareas)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu_tareas()

"""5. Escribe un programa tipo cajero automático que permita:
    a. Iniciar sesión a través de usuario y contraseña
    b. Realizar extracciones.
    c. Realizar depósitos.
    d. Salir"""
def iniciar_sesion(usuarios):
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == password:
        print(f"Bienvenido, {usuario}!")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False
def realizar_extraccion(saldo):
    monto = float(input("Ingrese el monto a extraer: "))
    
    if monto > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= monto
        print(f"Extracción de ${monto} realizada. Saldo restante: ${saldo}")
    return saldo   
def realizar_deposito(saldo):
    monto = float(input("Ingrese el monto a depositar: "))
    saldo += monto
    print(f"Depósito de ${monto} realizado. Saldo actual: ${saldo}")
    return saldo
def menu_cajero():
    usuarios = {'usuario1': 'password1', 'usuario2': 'password2'}
    saldo = 1000.0  # Saldo inicial
    
    if iniciar_sesion(usuarios):
        while True:
            print("\nMenú Cajero Automático:")
            print("1. Realizar Extracción")
            print("2. Realizar Depósito")
            print("3. Consultar Saldo")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                saldo = realizar_extraccion(saldo)
            elif opcion == '2':
                saldo = realizar_deposito(saldo)
            elif opcion == '3':
                print(f"Saldo actual: ${saldo}")
            elif opcion == '4':
                break
            else:
                print("Opción no válida, intente nuevamente.")

menu_cajero()
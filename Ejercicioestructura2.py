import numpy as np
def seleccion_menu():
    while True:
        opciones = input("Eliga una opción del menu.\n")
        if opciones.isdigit():
            opciones = int(opciones)
            return opciones
        else:
            print("Ingrese una opción válida\n")
            continue

def menu():
    print("ATENCION MEDICA VETERINARIA")
    print("\n˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ \n࣪")
    print("1- Crear ficha de la mascota.")
    print("2- Buscar por codigo de la mascota.")
    print("3- Eliminar por codigo de mascota.")
    print("4- Listar mascotas atentidas")
    print("5- Salir")
    print("\n˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ \n࣪")

def seleccion_rut():
    while True:
        try:
            rut = str(input("Ingrese el codigo de 3 digitos la mascota con guion: "))
            assert len(rut) == 4 and rut.find("-") == 2
            break
        except AssertionError:
            print("ERROR: Intentelo nuevamente.")
    return rut

def pacientesorden(i, j, pac):
    if j == 0:
        print("Nombre:", pac[i, j])
    elif j == 1:
        print("Codigo:", pac[i, j])
    elif j == 2:
        print("Edad:", pac[i, j])
    elif j == 3:
        print("Raza:", pac[i, j])
    elif j == 4:
        print("Especie:", pac[i, j])
    elif j == 5:
        print("Peso:", pac[i, j])
    elif j == 6:
        print("Diagnóstico:", pac[i, j])
    elif j == 7:
        print("Medicamentos recetados:", pac[i, j])

pac = np.empty([50, 8], dtype="object")
f = 0

while True:
    menu()
    opcion = seleccion_menu()
    
    if opcion == 1:
        for i in range(50):
            if pac[i, 1] is None:
                print("Ingrese el nombre de la mascota:")
                pac[i, 0] = input()
                x = seleccion_rut()
                pac[i, 1] = x
                print("Ingrese la edad de la mascota:")
                pac[i, 2] = input()
                print("Ingrese la raza de la mascota:")
                pac[i, 3] = input()
                print("Ingrese la especie de la mascota:")
                pac[i, 4] = input()
                print("Ingrese el peso de la mascota")
                pac[i, 5] = input()
                print("Ingrese el diagnostico de la mascota:")
                pac[i, 6] = input()
                print("Ingrese los medicamentos recetados::")
                pac[i, 7] = input()
                f += 1
                print("Paciente ingresado con éxito")
                break
        else:
            print("No hay espacio disponible para más pacientes")
    
    elif opcion == 2:
        x = seleccion_rut()
        for i in range(50):
            if pac[i, 1] == x:
                print("Paciente encontrado, sus datos son los siguientes:")
                for j in range(8):
                    pacientesorden(i, j, pac)
                break
        else:
            print("Paciente no encontrado")
        
    elif opcion == 3:
       
        print("Ingrese el codigo de la mascota para eliminar\n")
        x = seleccion_rut()
        for i in range(50):
            if pac[i, 1] == x:
                pac[i] = np.empty(7, dtype="object")  
                print("Paciente eliminado con éxito")
                break
        else:
            print("Paciente no encontrado")
        
    
    elif opcion == 4:
        for i in range(f):
            print("\n˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ \n࣪")
            print("Paciente:")
            for j in range(8):
                pacientesorden(i, j, pac)
    
    elif opcion == 5:
        break
    
    else:
        print("Ingrese una opción válida")

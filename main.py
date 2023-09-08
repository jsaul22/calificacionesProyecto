from os import system
import os

datosEstudiante = [[],[],[],[]]
datosDocente = [[],[],[]]
calificacionEstudiante = []
totalIndividual = []
numerocalificaciones = 0
numeroEstudiantes = 0
busquedalineal = 0
busquedabinaria = 0
busquedaInterpolacion = 0


def burbuja(arreglo):
  for fila in arreglo:
    n = len(fila)
    for i in range(n):
      for j in range(0, n-i-1):
        if fila[j] > fila[j+1]:
          fila[j], fila[j+1] = fila[j+1], fila[j]
def insercion(arreglo):
    for i in range(1, len(arreglo)):
        aux = arreglo[i]
        j = i - 1
        while j >= 0 and aux < arreglo[j]:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = aux

def imprimir(arreglo):
    for l in arreglo:
      insercion(l)

def algoritmoSeleccion(arreglo):
    n = len(arreglo)
    for i in range(n):
      aux = i
      for j in range(i+1, n):
        if arreglo[j] < arreglo[aux]:
          aux = j
        arreglo[i], arreglo[aux] = arreglo[aux], arreglo[i]

def imprimirSeleccion(arreglo):
  for x in arreglo:
    algoritmoSeleccion(x)

def quickSort(arreglo):
  if len(arreglo) <= 1:
    return arreglo

  auxp = arreglo[len(arreglo) // 2]
  izq = [x for x in arreglo if x < auxp]
  aux = [x for x in arreglo if x == auxp]
  der = [x for x in arreglo if x > auxp]

  return quickSort(izq) + aux + quickSort(der)



def guardarnotas(numerocalificaciones,numeroEstudiantes):
  calificaciones = open("reportes/calificaciones.txt", 'a')
  calificaciones.write("ESCUELA POLITECNICA NACIONAL".center(100) + "\n")
  calificaciones.write(f'{facultad}'.center(100) + "\n")
  calificaciones.write("REPORTE DE CALIFICACIONES\n".center(100) + "\n")
  calificaciones.write("Año lectivo: 2023-2024\n")
  calificaciones.write(f'Materia: {materia}\n')
  calificaciones.write("Nro"+ "Estudiante".center(20) + "Apellido".center(20) + "Correo".center(20))
  for i in range(numerocalificaciones):
    calificaciones.write(f'Nota {i+1}'.center(20))
  
  calificaciones.write("Total".center(20) + "\n")
  calificaciones.close()


def funcionBusqueda():
  busqueda = open("busqueda.txt", 'a')
  busqueda.write("ESCUELA POLITECNICA NACIONAL".center(100) + "\n")
  busqueda.write("REPORTE DE CALIFICACIONES".center(100) + "\n")
  busqueda.write("Busqueda de Calificaciones".center(100) + "\n")
  busqueda.write("ALGORITMO: Lineal / Binaria / Interpolación\n")
  busqueda.write("\n")
  busqueda.close()
  
  
def funcionOrdenar():
  ordenar = open("ordenamiento.txt", 'a')
  ordenar.write("ESCUELA POLITECNICA NACIONAL".center(100) + "\n")
  ordenar.write("REPORTE DE CALIFICACIONES".center(100) + "\n")
  ordenar.write("Calificaciones Ordenadas".center(100) + "\n")
  ordenar.write("ALGORITMO: Brubuja / Heap Sort / Merge Sort / Quick Sort\n")
  ordenar.write("\n")


def ValidacionIngreso(usuario,password):
  while(usuario!="docente@esfot.edu.ec" or password!="Docentes2023*"):
    print("----SAEW-----")
    print("Se ingresó mal el usuario o la contraseña \nIntente nuevamente sus credenciales\n")
    usuario=input("Ingrese su usuario: ")
    password=input("Ingrese su contraseña: ")
    system("clear")

def main():
  opciones = 0
  print("----SAEW-----\nIngrese sus credenciales\n")
  usuario=input("Ingrese su usuario: ")
  password=input("Ingrese su contraseña: ")
  system("clear")
  ValidacionIngreso(usuario,password)
  print("\t\tBIENVENIDO")
  print()
  while opciones != 4:
    print("1. Ingresar datos Docente-Estudiante")
    print("2. Ordenar datos Docente-Estudiante")
    print("3. Buscar datos Docente-Estudiante")
    print("4. Salir")
    opciones = int(input("Ingrese la opcion que desea: " ))
    if (opciones == 1):
      calificacionesTotal = 0
      numAprobados = 0
      numSuspenso = 0
      numReprobados = 0
      aux = 0
      aux2 = 0
      opcion1 = "aux"
      while (opcion1 != "c"):
        print("a) Registrar datos del profesor, materia, estudiantes y sus calificaciones")
        print("b) Guardar la información en un archivo plantilla “calificaciones.txt”")
        print("c) Salir")
        opcion1 = input("Ingrese una opcion.... a/b/c: ").lower()
        if (opcion1 == "a"):
          print("---------------BIENVENIDO--------------------")
          print("Registre los datos del DOCENTE: ")
          nombreDocente = input("Ingrese el nombre del DOCENTE: ")
          facultadDocente = input("Ingrese la facultad del DOCENTE: ")
          materia = input("Ingrese la materia del DOCENTE: ")
          datosDocente[0].append(nombreDocente)
          datosDocente[1].append(facultadDocente)
          datosDocente[2].append(materia)
          nombre = datosDocente[0][0]
          facultad = datosDocente[1][0]
          materia = datosDocente[2][0]
          print()
          print("Ingrese los datos de sus ESTUDIANTES ")
          numeroEstudiantes= int(input("Cuantos estudiantes desea ingresar: "))
          numerocalificaciones = int(input("cuantas calificaciones desea ingresar: "))
          calificacionEstudiante = [[] for i in range(numeroEstudiantes)]
          totalIndividual = [[] for i in range(numeroEstudiantes)]
          for i in range(numeroEstudiantes):
            nombreEstudiante = input(f'Ingrese el nombre del Estudiante Nro {i+1}: ')
            apellidoEstudiante = input(f'Ingrese el apellido del Estudiante {nombreEstudiante}: ')
            correoEstudiante = input(f'Ingrese el correo del estudiante {nombreEstudiante} {apellidoEstudiante}: ')
            
            datosEstudiante[0].append(nombreEstudiante)
            datosEstudiante[1].append(apellidoEstudiante)
            datosEstudiante[2].append(correoEstudiante)
            print(f'Ingrese las calificaciones del estudiante Nro {i+1}')
            print()
            for j in range(numerocalificaciones):
              calificacion = float(input(f'Calificacion Nro {j+1}: '))
              while calificacion >20 or calificacion < 0:
                print("Por favor ingrese una calificacion de 0-20...")
                print()
                calificacion = float(input(f'Calificacion Nro {j+1}: '))  
              calificacionesTotal += calificacion 
              aux2 += calificacion
              
              calificacionEstudiante[i].append(calificacion)

            promedioaux2 = aux2/numerocalificaciones
            totalIndividual[i].append(promedioaux2)
            aux3 = aux2/numerocalificaciones
            
            if (aux3 >= 14 and aux3 <=20 ):
              numAprobados += 1
            if (aux3 >= 9 and aux3 <= 13):
              numSuspenso += 1
            if (aux3 >= 1 and aux3 <= 8):
              numReprobados += 1
              
            aux2 = 0
            aux3 = 0
          promedioGeneral = calificacionesTotal/numeroEstudiantes
        elif opcion1 == "b":
          calificaciones = open('reportes/calificaciones.txt', 'a')
          for i in range(numeroEstudiantes):
            calificaciones.write(str(i+1))
            calificaciones.write(datosEstudiante[0][i].center(22))
            calificaciones.write(datosEstudiante[1][i].center(22))
            calificaciones.write(datosEstudiante[2][i].center(20))
            for j in range(numerocalificaciones):
              calificaciones.write(str(calificacionEstudiante[i][j]).center(20))
            calificaciones.write(str(totalIndividual[i]).center(20) + "\n")
          calificaciones.write("\n")
          calificaciones.write("RESUMEN\n")
          calificaciones.write("Promedio del curso")
          calificaciones.write(str(promedioGeneral).center(60) + "\n")
          calificaciones.write("Aprobados (14-20)".center(100))
          calificaciones.write(str(numAprobados).center(20) + "\n")
          calificaciones.write("Suspenso (09-13)".center(100))
          calificaciones.write(str(numSuspenso).center(20) + "\n")
          calificaciones.write("Reprobados (01-08)".center(100))
          calificaciones.write(str(numReprobados).center(20) + "\n")
          calificaciones.write("\n")
          calificaciones.write("--------------------------------".center(100) + "\n")
          calificaciones.write(nombre.center(100) + "\n")
          calificaciones.write("-------------".center(100) + "\n")
          calificaciones.write("-------------".center(100) + "\n")
          calificaciones.close()
          print("Se guardó exitosamente en calificaciones.txt")
          print()
    elif (opciones==2):
      opc = "aux"
      while opc != "d":
        
        print("--------Bienvenido a nuestro submenú-------")
        print("a. Ordenar las calificaciones de los estudiantes en base a un algoritmo\nb. Guardar la información en un archivo plantilla 'ordenamiento.txt'\nc. Mostrar la información del archivo en la consola del programa\nd. Salir al menu principal")
        opc=input("Ingrese el literal: ").lower()
        if opc=="a":
          print("--------Bienvenido a nuestro submenú-------")
          print("1.Burbuja\n2. Inserción\n3.Selección\n4. MergeSort\n5.QuickSort")
          opcLiteral=int(input("Ingrese una opción: "))
          if opcLiteral==1:
            print("1. Burbuja")
            burbuja(calificacionEstudiante)
            print("Las calificaciones ordenadas son:")
            for i in calificacionEstudiante: 
              print(i)
            print()
      
          elif opcLiteral==2:
            print("2.Inserción")
            imprimir(calificacionEstudiante)
            for lineas in calificacionEstudiante:
              print(lineas)
            print()
      
          elif opcLiteral==3:
            print("3.Selección")
            imprimirSeleccion(calificacionEstudiante)
            for i in calificacionEstudiante:
              print(i)
            print()
      
          elif opcLiteral==4:
            print("4.MergeSort")
            lista_ordenada = mergesort(calificacionEstudiante)
            for l in calificacionEstudiante:
               print(l)
            print()
          elif opcLiteral==5:
            print("5.QuickSort")
            quickSort(calificacionEstudiante)
            for i in range(len(calificacionEstudiante)):
              calificacionEstudiante[i] = quickSort(calificacionEstudiante[i])  
            for i in calificacionEstudiante:
              print(i)
            print()
        elif opc == "b":
          print("1. Burbuja\n2. Inserción\n3. Selección\n4. MergeSort\n5. QuickSort")
          opcionOrdenar = int(input("Ingrese el metodo de busqueda que desea guardar en un archivo: "))
          
          funcionOrdenar()
          if opcionOrdenar == 1:
            print("eligio Burbuja...")
            ordenar = open("ordenamiento.txt", 'a')
            ordenar.write("\n")
            ordenar.write("Orden por burbuja \n")
            burbuja(calificacionEstudiante)
            ordenar.write("Las calificaciones ordenadas son:\n")
            for i in calificacionEstudiante: 
              ordenar.write(str(i))
            ordenar.close()
            print()
          elif opcionOrdenar == 2:
            print("eligio Inserción...")
            ordenar = open("ordenamiento.txt", 'a')
            ordenar.write("\n")
            ordenar.write("Orden por Inserción \n")
            imprimir(calificacionEstudiante)
            ordenar.write("Las calificaciones ordenadas son:\n")
            for lineas in calificacionEstudiante:
              ordenar.write(str(lineas))
            ordenar.write("\n")
            ordenar.close()
            print()
          elif opcionOrdenar == 3:
            print("eligio Selección...")
            ordenar = open("ordenamiento.txt", 'a')
            ordenar.write("\n")
            ordenar.write("Orden por Selección \n")
            imprimirSeleccion(calificacionEstudiante)
            ordenar.write("Las calificaciones ordenadas son:\n")
            for i in calificacionEstudiante:
              ordenar.write(str(i))
            ordenar.write("\n")
            ordenar.close()
            print()
          elif opcionOrdenar==4:
            print("eligio MergeSort")
            ordenar = open("ordenamiento.txt", 'a')
            ordenar.write("\n")
            lista_ordenada = mergesort(calificacionEstudiante)
            for l in calificacionEstudiante:
               ordenar.write(str(l))
            print()
            ordenar.close()
          elif opcionOrdenar == 5:
            print("eligio QuickSort...")
            ordenar = open("ordenamiento.txt", 'a')
            ordenar.write("\n")
            ordenar.write("Orden por QuickSort \n")
            quickSort(calificacionEstudiante)
            ordenar.write("Las calificaciones ordenadas son:\n")
            for i in range(len(calificacionEstudiante)):
              calificacionEstudiante[i] = quickSort(calificacionEstudiante[i])  
            for i in calificacionEstudiante:
              ordenar.write(str(i))
            ordenar.write("\n")
            ordenar.close()
            print()
        elif opc == "c":
          print("Mostrar la información del archivo en la consola del programa.")
          ordenar = open("ordenamiento.txt", 'r')
          lineas = ordenar.readlines()
          for l in lineas:
            print(l, end="")
          print()
          ordenar.close()
          print()
    elif (opciones == 3):
      opc = "aux"
      while opc != "d":
        print("--------Bienvenido a nuestro submenú-------")
        print("a. Buscar una calificación.\nb. Almacenar los resultados en un archivo plantilla “búsqueda.txt” \nc. Mostrar la información del archivo en la consola del programa\nd. Salir al menu principal")
        opc=input("Ingrese una opcion: ").lower()
        if opc=="a":
          print("--------Bienvenido a nuestro submenú-------")
          print("1.Lineal \n2. Binaria\n3.Interpolación")
          opc=int(input("Ingrese una opción: "))
          if opc==1:
            print("1. Lineal")
            print()
            auxi=0
            elemento=int(input("Ingrese la calificación a buscar: "))
            busquedalineal = elemento
            for i in range(numeroEstudiantes):
              if elemento in calificacionEstudiante[i]:
                auxi= 1    
                print(f'Estudiante Nro {i+1}')
                print(f"La calificacion {elemento} corresponde al estudiante: \n")
                print("Nombre: ",datosEstudiante[0][i])
                print("Apellido: ",datosEstudiante[1][i])
                print("Correo electronico:",datosEstudiante[2][i])       
              if auxi != 1:
                print(f"El valor {elemento} no se encuentra en el arreglo")
            print()
          elif opc==2:
            print("2. Binaria")
            print()
            for i in range(numeroEstudiantes):
              calificacionEstudiante[i].sort()
            elemento = float(input("Ingrese la calificación a buscar: "))
            busquedabinaria = elemento
            auxi = 0 
            for i in range(numeroEstudiantes):
              izquierda = 0
              derecha = numerocalificaciones - 1
              while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                if calificacionEstudiante[i][medio] == elemento:
                  auxi = 1
                  print(f"La calificación {elemento} corresponde al estudiante:")
                  print("Nombre:", datosEstudiante[0][i])
                  print("Apellido:", datosEstudiante[1][i])
                  print("Correo electrónico:", datosEstudiante[2][i])
                  break
                elif calificacionEstudiante[i][medio] < elemento:
                  izquierda = medio + 1
                else:
                  derecha = medio - 1
            
            if auxi != 1:
                print(f"El valor {elemento} no se encuentra en el arreglo.")
            print()
          elif opc==3:
            print("3. Interpolación")
            for i in range(numeroEstudiantes):
              calificacionEstudiante[i].sort()
  
            elemento = int(input("Ingrese la calificación a buscar: "))
            busquedaInterpolacion = elemento
            auxi = 0
            
            for i in range(numeroEstudiantes):
              calificacionEstudiantedos = calificacionEstudiante[i]
              izquierda = 0
              derecha = numerocalificaciones - 1
            
              while izquierda <= derecha and calificacionEstudiantedos[izquierda] <= elemento <= calificacionEstudiantedos[derecha]:
                posicion= izquierda + ((derecha - izquierda) * (elemento - calificacionEstudiantedos[izquierda])) // (calificacionEstudiantedos[derecha] - calificacionEstudiantedos[izquierda])
            
                if calificacionEstudiantedos[int(posicion)] == elemento:
                  auxi = 1
                  print(f"La calificación {elemento} corresponde al estudiante:")
                  print("Nombre:", datosEstudiante[0][i])
                  print("Apellido:", datosEstudiante[1][i])
                  print("Correo electrónico:", datosEstudiante[2][i])
                  break
                elif calificacionEstudiantedos[posicion] < elemento:
                  izquierda = posicion + 1
                else:
                  derecha = posicion
            if auxi != 1:
              print(f"El valor {elemento} no se encuentra en el arreglo.")
            print()
      
        elif opc=="b":
        
          print("b. Almacenar los resultados en un archivo plantilla “busqueda.txt")
          print("1.Lineal \n2. Binaria\n3.Interpolación")
          opcionbusqueda = int(input("Ingrese el metodo de busqueda que desea guardar en un archivo: "))
          funcionBusqueda()
          
          if opcionbusqueda == 1:
            print("eligio lineal...")
            busqueda = open("busqueda.txt", 'a')
            busqueda.write("Busqueda Lineal \n")
            auxi=0
            for i in range(numeroEstudiantes):
              if busquedalineal in calificacionEstudiante[i]:
                auxi = 1
                busqueda.write(f'Estudiante Nro {i+1}\n')
                busqueda.write(f'La calificacion {busquedalineal} corresponde al estudiante:\n')
                busqueda.write(f'Nombre: {datosEstudiante[0][i]}\n')
                busqueda.write(f'Apellido: {datosEstudiante[1][i]}\n')
                busqueda.write(f'Correo electronico: {datosEstudiante[2][i]}\n') 
            if auxi != 1:
              busqueda.write(f'El valor {busquedalineal} no se encuentra en el arreglo\n')
            busqueda.close()
            print()
          elif opcionbusqueda == 2:
            print("eligio binaria...")
            busqueda = open("busqueda.txt", 'a')
            busqueda.write("\n")
            busqueda.write("Busqueda Binaria \n")
            for i in range(numeroEstudiantes):
              calificacionEstudiante[i].sort()
            auxi = 0 
            for i in range(numeroEstudiantes):
              izquierda = 0
              derecha = numerocalificaciones - 1
              while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                if calificacionEstudiante[i][medio] == busquedabinaria:
                  auxi = 1
                  busqueda.write(f'La calificación {busquedabinaria} corresponde al estudiante:\n')
                  busqueda.write(f'Nombre: {datosEstudiante[0][i]}\n')
                  busqueda.write(f'Apellido: {datosEstudiante[1][i]}\n')
                  busqueda.write(f'Correo electrónico: {datosEstudiante[2][i]}\n')
                  break
                elif calificacionEstudiante[i][medio] < busquedabinaria:
                  izquierda = medio + 1
                else:
                  derecha = medio - 1
            
            if auxi != 1:
                busqueda.write(f'El valor {busquedabinaria} no se encuentra en el arreglo.')
            busqueda.close()
            print()
          elif opcionbusqueda == 3:
            print("eligio Interpolacion...")
            busqueda = open("busqueda.txt", 'a')
            busqueda.write("Busqueda Interpolacion \n")
            for i in range(numeroEstudiantes):
              calificacionEstudiante[i].sort()
            auxi = 0
            for i in range(numeroEstudiantes):
              calificacionEstudiantedos = calificacionEstudiante[i]
              izquierda = 0
              derecha = numerocalificaciones - 1
            
              while izquierda <= derecha and calificacionEstudiantedos[izquierda] <= busquedaInterpolacion <= calificacionEstudiantedos[derecha]:
                posicion= izquierda + ((derecha - izquierda) * (busquedaInterpolacion - calificacionEstudiantedos[izquierda])) // (calificacionEstudiantedos[derecha] - calificacionEstudiantedos[izquierda])
            
                if calificacionEstudiantedos[int(posicion)] == busquedaInterpolacion:
                  auxi = 1
                  busqueda.write(f'La calificación {busquedaInterpolacion} corresponde al estudiante:\n')
                  busqueda.write(f'Nombre: {datosEstudiante[0][i]}\n')
                  busqueda.write(f'Apellido: {datosEstudiante[1][i]}\n')
                  busqueda.write(f'Correo electrónico: {datosEstudiante[2][i]}\n')
                  break
                elif calificacionEstudiantedos[posicion] < busquedaInterpolacion:
                  izquierda = posicion + 1
                else:
                  derecha = posicion
            if auxi != 1:
              print(f'El valor {busquedaInterpolacion} no se encuentra en el arreglo\n')
            busqueda.close()
            print()
        elif opc=="c":
          print("Mostrar la información del archivo en la consola del programa.")
          busqueda = open("busqueda.txt", 'r')
          lineas = busqueda.readlines()
          for l in lineas:
            print(l, end="")
          print()
          busqueda.close()
  print("Gracias por utilizar nuestro servicio")
main()
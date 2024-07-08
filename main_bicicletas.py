from funciones_bicicletas import *
"""
Enunciado: Se dispone de un archivo con datos acerca de los participantes de una carrera de bicicletas, que tiene el siguiente formato: 
id_bike, nombre (del dueño), tipo (bmx, playera, mtb, paseo), tiempo por ejemplo: 
50,jorge,bmx,0
51,sofia,paseo,0
52,andrea,mtb,0  
Se deberá realizar un programa que permita el análisis de dicho archivo. 
El programa contará con el siguiente menú:  
1) Cargar archivo CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios los elementos del mismo. 
2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las bicicletas. 
3) Asignar tiempos: Se deberá mapear la lista con una función que asignará a cada bicicleta un valor de tiempo entre 50 y 120 minutos calculado de manera aleatoria y se mostrará por pantalla la lista. 
4) Informar ganador: Informar el nombre del dueño de la bicicleta que llego primero y el tiempo que tardo. Si hubiera empate. informar todos los nombres de las bicicletas que empataron. 
5) Filtrar por tipo: Se deberá pedir un tipo de bicicleta al usuario y escribir un archivo igual al original, pero donde solo aparezcan bicicletas del tipo seleccionado. El nombre del archivo será por ejemplo playeras.csv 
6) Informar promedio por tipo: Listar el promedio de tiempo por cada tipo de bicicleta. 
7) Mostrar posiciones: Se deberá mostrar por pantalla un listado de las bicicletas ordenadas por tipo y dentro de las del mismo tipo que aparezcan ordenadas por tiempo ascendente. 
8) Guardar posiciones: Se deberá guardar el listado del punto anterior en un archivo JSON. 
9) Salir. 
"""
lista_bicicletas = []
lista_posiciones = []
lista_ordenada = []
while True:
  match menu():
    case "1":
      lista_bicicletas = cargar_archivo_csv("bicicletas.csv")
      print("¡Lista de bicicletas cargada!")

    case "2":
      mostrar_bicicletas(lista_bicicletas)

    case "3":
      mapear_tiempos(lista_bicicletas)
      for bicicleta in lista_bicicletas:
        nombre = bicicleta["nombre"]
        tiempo = bicicleta["tiempo"]
        print("-------------------------------------------------------------")
        print(f"Nombre: {nombre} - tiempo: {tiempo}")

    case "4":
      filtrar_mejores_tiempos(lista_bicicletas, lista_posiciones)
      for bicicleta in lista_posiciones:
        nombre = bicicleta["nombre"]
        tiempo = bicicleta["tiempo"]
        tipo = bicicleta["tipo"]
        print("-------------------------------------------------------------")
        print(f"Nombre: {nombre} - Tipo:{tiempo} - Tiempo: {tiempo}")


    case "5":
      tipo = input("Ingrese un tipo de bicicleta (bmx/playera/mtb/paseo): ")
      filtrar_por_tipo(lista_bicicletas, tipo)

    case "6":
      tipos_bicicleta = mapear_tipos_bicicleta(lista_bicicletas)

      for tipo in tipos_bicicleta:
        tipo_bicicletas = flitrar_bicicletas_por_tipo(lista_bicicletas, tipo)
        promedio = promedio_tiempo_bicicletas(tipo_bicicletas)
        print(f"Tiempo {promedio:.2f} - Tipo: {tipo}")
        print("------------------------------------------------")

    case "7":
      ordenar_clave_criterio(lista_bicicletas, "tipo", "tiempo", lista_ordenada)
      mostrar_bicicletas(lista_bicicletas)

    case "8":
      guardar_en_json(lista_ordenada)
      print("La lista con las bicicletas ordenadas fue guardada exitosamente.")
    
    case "9":
      break
 
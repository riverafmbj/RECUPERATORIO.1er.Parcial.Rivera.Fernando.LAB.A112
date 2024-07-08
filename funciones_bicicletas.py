from random import randint

def get_path_actual(nombre_archivo):
  """
  Obtiene el path del archivo que le pasemos

  Args:
      nombre_archivo(str): el nombre del archivo

  Returns:
      el directorio donde se encuentra el archivo
  """  
  
  import os
  directorio_actual = os.path.dirname(__file__)
  return os.path.join(directorio_actual, nombre_archivo)

def menu()->str:
  """
  Imprime el menú en pantalla

  Returns:
      input: para seleccionar la opción que querramos
  """
  
  print(f"{'Menú de opciones':^50}")
  print("1 - Cargar archivo .CSV")
  print("2 - Imprimir lista de bicicletas")
  print("3 - Asignar tiempos")
  print("4 - Mostrar mejores tiempos")
  print("5 - Filtrar por tipo")
  print("6 - Promedio de tiempo por tipo de bicicletas")
  print("7 - Ordenar bicicletas por tipo y tiempo ascendente")
  print("8 - Guardar bicicletas ordenadas por tipo y tiempo ascendente")
  print("9 - Salir")

  return input("Ingrese opción: ")

def cargar_archivo_csv(nombre_archivo:str)->list:
  """
  Carga los datos de un archivo en una lista

  Args:
      nombre_archivo(str): el nombre del archivo

  Returns:
      lista_bicicletas(list): la lista con los datos cargados
  """
  with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
    lista_bicicletas = []
    encabezado = archivo.readline().strip("\n").split(",")
    

    for linea in archivo.readlines(): #o for linea in archivo.readlines():
      bicicleta = {}
      linea = linea.strip("\n").split(",")
      
      id, nombre, tipo, tiempo = linea
      bicicleta["id"] = id
      bicicleta["nombre"] = nombre
      bicicleta["tipo"] = tipo
      bicicleta["tiempo"] = tiempo
      lista_bicicletas.append(bicicleta)
  
    return lista_bicicletas
  
def mostrar_bicicletas(lista_bicicletas:list)->None:
  """
  Imprime en pantalla la lista de bicicletas

  Args:
      lista_bicicletas(list): la lista con los datos cargados
  """
  tam = len(lista_bicicletas)
  print("                 ***Listado de bicicletas***")
  print("ID                  Nombre                 Tipo      Tiempo")
  print("---------------------------------------------------------------")

  for i in range(tam):
    mostrar_bicicleta_item(lista_bicicletas[i])

def mostrar_bicicleta_item(bicicleta: dict)->None:
  """
  Imprime en pantalla una bicicleta

  Args:
      bicicleta(dict): el diccionario con los datos de la bicicleta
  """
  print(f"{bicicleta['id']:>3} {bicicleta['nombre']:>30} {bicicleta['tipo']:>15} {bicicleta['tiempo']:>10}")

def asignar_tiempo()->int:
  """
  Asigna un número de tiempo random

  Return:
      tiempo(int): un número int random
  """
  tiempo = randint(50, 120)
  return tiempo

def mapear_tiempos(lista_bicicletas)->list:
   """
   Mapea la lista de bicicletas con los tiempos

   Args:
      lista_bicicletas(list): la lista con las bicicletas

   Returns:
      lista_mapeada(list): la lista con los tiempos mapeados
   """
   lista_mapeada = []
   for bicicleta in lista_bicicletas:
     bicicleta["tiempo"] = asignar_tiempo()
     lista_mapeada.append({bicicleta["nombre"], bicicleta["tiempo"]})
   return lista_mapeada

def filtrar_por_tipo(lista_bicicletas:list, tipo:str)->None:
  """
   Filtra a la lista de bicicletas por tipo y crea un archivo .csv con las bicicletas de ese tipo

   Args:
      lista_bicicletas(list): la lista con las bicicletas
      tipo(str): la clave "tipo" de los diccionarios de las bicicletas

   Returns:
      None
   """
  tipo = tipo.lower()
  bicicletas_filtradas = []

  for bicicleta in lista_bicicletas:
      if tipo == bicicleta["tipo"].lower():
          bicicletas_filtradas.append(bicicleta)
  

  with open(get_path_actual(f"{tipo}.csv"), "w", encoding="utf-8") as archivo:
        values = list(lista_bicicletas[0].keys())
        encabezado = ",".join(values) + "\n" #lo uno con comas y le agrego el \n
        archivo.write(encabezado)
        for bicicleta in bicicletas_filtradas:
          values = list(bicicleta.values())
          l = []
          for value in values:
              if isinstance(value, int):
                  l.append(str(value))
              elif isinstance(value, float):
                  l.append(str(value))
              else:
                  l.append(value)
          linea = ",".join(l) + "\n"
          archivo.write(linea)

def ordenar_clave_criterio(lista_bicicletas:list, clave:str, clave2:str, lista_vacia)->None:
  """
   Ordena la lista por 2 criterios y luego la guarda en una lista vacía

   Args:
      lista_bicicletas(list): la lista con las bicicletas
      clave(str): la clave del diccionario que será el primer criterio de ordenamiento
      clave2(str): la clave del diccionario que será el segundo criterio de ordenamiento
      lista_vacía(list): la lista vacía donde se guardarán los datos ordenados

   Returns:
      None
   """
  
  tam = len(lista_bicicletas)
  for i in range(len(lista_bicicletas)):
    for j in range (i + 1, tam):
        if lista_bicicletas[i][clave] > lista_bicicletas[j][clave] or \
        (lista_bicicletas[i][clave] == lista_bicicletas[j][clave] and lista_bicicletas[i][clave2] > lista_bicicletas[j][clave2]):
          aux = lista_bicicletas[i]
          lista_bicicletas[i] = lista_bicicletas[j]
          lista_bicicletas[j] = aux
    lista_vacia.append(lista_bicicletas[i])

def filtrar_mejores_tiempos(lista_bicicletas:list, lista_vacia:list)->None:
  """
   Filtra a las bicicletas con mejor tiempo en una lista vacía

   Args:
      lista_bicicletas(list): la lista con las bicicletas
      lista_vacia(list): la lista vacía a la cual irán las bicicletas con mejor tiempo

   Returns:
      None
   """
  tiempo_min = 0
  flag_tiempo = False

  for bicicleta in lista_bicicletas:
    
    tiempo = bicicleta["tiempo"]
    if flag_tiempo == False or tiempo < tiempo_min:
      tiempo_min = tiempo
      flag_tiempo = True

  if flag_tiempo == True:
    for bicicleta in lista_bicicletas:
      tiempo = bicicleta["tiempo"]
      if tiempo == tiempo_min:
        lista_vacia.append(bicicleta)

def lista_sin_repetidos(lista_repetidos:list)->list:
  """
   Devuelve una lista sin índices repetidos

   Args:
      lista_repetidos(list): la lista con los índices repetidos

   Returns:
      list: la lista sin repetidos
   """
  return list(set(lista_repetidos))

def mapear_tipos_bicicleta(lista:list)->list:
   """
   Mapea una lista vacía con los tipos de bicicleta sin repetir

   Args:
      lista(list): la lista de bicicletas

   Returns:
      list: la lista con los tipos de bicicleta sin repetir
   """
   lista_mapeada = []
   for bicicleta in lista:
     lista_mapeada.append(bicicleta["tipo"])
   return lista_sin_repetidos(lista_mapeada)

def promedio_campo_bicicletas(lista:list, campo:str)->float:
  """
   Calcula el promedio de un campo de una lista

   Args:
      lista(list): la lista de bicicletas
      campo(str): el campo a calcular
   Returns:
      promedio(float): el promedio calculado. Si el largo de la lista es menor a 0, devuelve 0.0
  """
  acumulador = 0
  cantidad = len(lista)
  if cantidad > 0:
   for bicicleta in lista:
     acumulador += bicicleta[campo]
   promedio = acumulador / cantidad
   return promedio  
  return 0.0

def promedio_tiempo_bicicletas(lista:list)->float:
  """
   Calcula el promedio de los tiempos de las bicicletas

   Args:
      lista(list): la lista de bicicletas
   Returns:
      promedio(float): el promedio de los tiempos calculado.
  """
  return promedio_campo_bicicletas(lista, "tiempo")

def flitrar_bicicletas_por_tipo(lista:list, tipo:str)->list:
  """
   Filtra la lista de bicicletas por el tipo de bicicleta en una lista vacía

   Args:
      lista(list): la lista de bicicletas
   Returns:
      lista_filtrada(list): la lista filtrada con los tipos de bicicleta
  """
  lista_filtrada = []
  for bicicleta in lista:
    if bicicleta["tipo"] == tipo:
      lista_filtrada.append(bicicleta)
  return lista_filtrada

def guardar_en_json(lista_bicicletas:list)->None:
  """
   Crea un archivo .json y allí guarda el listado de bicicletas ordenadas

   Args:
      lista_bicicletas(list): la lista con las bicicletas

   Returns:
      None
   """
  import json 
  with open(get_path_actual("bicicletas_ordenadas.json"), "w", encoding="utf-8") as archivo:
      json.dump(lista_bicicletas, archivo, indent=4) 





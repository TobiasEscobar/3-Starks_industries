from data_stark import lista_personajes

def stark_normalizar_datos(lista:list):
    '''
    Brief:
    -
    Param:
    -
    Return:
    -
    '''
    if len(lista) == 0:
        datos_modificados = False
        print("Error. Lista de datos vacia")
    else:
        datos_modificados = False
        for data in lista:
            if (type(data['altura']) != float):
                data['altura'] = float(data['altura'])
                datos_modificados = True
            if (type(data['peso']) != float):
                data['peso'] = float(data['peso'])
                datos_modificados = True
            if (type(data['fuerza']) != int):
                data['fuerza'] = int(data['fuerza'])
                datos_modificados = True
            
        if datos_modificados == True:
            print("Datos normalizados")


# 1.1. 
def obtener_dato(dict_heroe:dict, clave:str)->dict:
    '''
    Brief:
    - Permite obtener un valor específico de un diccionario que representa a un heroe
    Param:
    - dict_heroe: Un diccionario que representa a un heroe el cual debe contener información sobre el superhéroe, incluyendo la clave que se busca.
    - clave: Un string que especifica la clave que se desea obtener del diccionario.
    Return:
    - Puede devolver False dependiendo del caso o el valor de la clave que se buscaba
    '''
    if len(dict_heroe) == 0 or "nombre" not in dict_heroe:
        return False
    if clave in dict_heroe:
        return dict_heroe[clave]
    else:
        return False


# 1.2 
def obtener_nombre(dict_heroe:dict)->str:
    '''
    Brief:
    - Utilizando la funcion obtener_dato() esta funcion devolvera el nombre de un heroe que se le especifique
    Param:
    - dict_heroe: Un diccionario que representa a un heroe el cual debe contener información sobre el superhéroe, incluyendo la clave que se busca.
    Return:
    - Devuelve False si el nombre no existe o muestra por consola el nombre del heroe
    '''
    nombre = obtener_dato(dict_heroe, "nombre")
    if nombre:
        mensaje = print(f"Nombre: {nombre}")
        return mensaje
    else:
        return False


# 2. 
def obtener_nombre_y_dato(dict_heroe:dict, key:str)->str:
    '''
    Brief:
    - Esta funcion llama a las dos funciones anteriores para mostrar el nombre de un heroe y una caracteristica con su respectivo valor
    Param:
    - dict_heroe: Un diccionario que representa a un heroe el cual debe contener información sobre el superhéroe, incluyendo la clave que se busca.
    - key: Un string que especifica la clave que se desea obtener del diccionario.
    Return:
    - Devuelve False si el nombre no existe o muestra por consola el nombre del heroe
    '''
    nombre = obtener_nombre(dict_heroe)
    valor = obtener_dato(dict_heroe, key)
    if nombre and valor:
        mensaje = print(f"Nombre: {nombre} | {key}: {valor}")
        return mensaje
    else:
        return False

# 3.1 
#key = altura, peso etc
def obtener_maximo(lista:list, key:str)->float:
    '''
    Brief:
    - Busca el maximo de un valor que se le especifique
    Param:
    - lista: Lista donde debe iterar para hacer la busqueda del valor
    - key: Un string que especifica la clave que se desea obtener del diccionario.
    Return:
    - Devuelve el maximo valor encontrado o False si es igual a 0
    '''
    primer_flag = True
    if len(lista) == 0: 
        return False
    for heroe in lista:
        if type(heroe) == dict and key in heroe:
            valor = heroe[key]
            if type(valor) == int or type(valor) == float:
                if primer_flag == True or valor > max_valor:
                    max_valor = valor
                    primer_flag = False
    if max_valor != 0:
        return max_valor
    else:
        return False


def obtener_minimo(lista:list, key:str)->float:
    '''
    Brief:
    - Busca el minimo de un valor que se le especifique
    Param:
    - lista: Lista donde debe iterar para hacer la busqueda del valor
    - key: Un string que especifica la clave que se desea obtener del diccionario.
    Return:
    - Devuelve el minimo valor encontrado o False si es igual a 0
    '''
    primer_flag = True
    if len(lista) == 0: 
        return False
    for heroe in lista:
        if type(heroe) == dict and key in heroe:
            valor = heroe[key]
            if type(valor) == int or type(valor) == float:
                if primer_flag == True or valor < min_valor:
                    min_valor = valor
                    primer_flag = False
    if min_valor != 0:
        return min_valor
    else:
        return False


def obtener_dato_cantidad(lista:list, numero_a_buscar:str, key:str)->list:
    '''
    Brief:
    - Esta función busca heroes en una lista que tienen un valor específico con la clave que se le especifique.
    Param:
    - lista: Una lista de heroes representados como diccionarios 
    - numero_a_buscar: Un string que especifica si se deben buscar heroes con el valor "maximo" o "minimo" en la clave especificada.
    - key: Un string que especifica la clave sobre la que se realizara la busqueda.
    Return:
    - Una lista de nombres de los heroes que tienen el valor máximo o mínimo en la clave dicha
    '''

    heroes_encontrados = []
    if numero_a_buscar == "maximo":
        num_maximo = obtener_maximo(lista, key)
        for heroe in lista:
            numero_heroe = heroe[key]
            if numero_heroe == num_maximo:
                nombre = obtener_nombre(heroe)
                heroes_encontrados.append(nombre)
    
    elif numero_a_buscar == "minimo":
        num_minimo = obtener_minimo(lista, key)
        for heroe in lista:
            numero_heroe = heroe[key]
            if numero_heroe == num_minimo:
                nombre = obtener_nombre(heroe)
                heroes_encontrados.append(nombre)

    return heroes_encontrados


def stark_imprimir_heroes(lista:list)->str:
    '''
    Brief:
    - Esta función se utiliza para imprimir información sobre los superhéroes de una lista, uno por uno.
    Param:
    - lista: Una lista de heroes representados como diccionarios
    Return:
    - Si la lista está vacía la función devuelve `False` para indicar que no se pudo imprimir ningún heroe.
    - Si la lista contiene al menos un superhéroe, lo mostrara en consola. 
    '''

    if len(lista) < 1:
        return False
    else:
        for heroe in lista:
            return heroe


# 4.1 
def sumar_dato_heroe(lista:list, key:str)->float:
    '''
    Brief:
    - Calcula la suma de los valores numéricos de una clave específica en los diccionarios que representan a los heroes en una lista.
    Param:
    - lista: Una lista de superhéroes representados como diccionarios. 
    - key: Un string que especifica la clave sobre la que se realizará la suma.
    Return:
    - Devuelve la suma de los valores numéricos de la clave especificada en los diccionarios de la lista. 
    - Si no se encuentran valores numéricos en la clave o si la lista está vacía, la función devuelve 0.
    '''
    suma = 0  
    for heroe in lista:
        if type(heroe) == dict and key in heroe:
            valor = heroe[key]
            if type(valor) == int or type(valor) == float:
                suma += valor

    return suma


# 4.2 
def dividir(dividendo:float, divisor:float)->float:
    '''
    Brief:
    - Divide dos numeros que se les pase por parametro y lo devuelve
    Param:
    - dividiendo: numero a dividir
    - divisor: numero que divide al otro y que no puede ser un 0
    Return: 
    - Devuelve el resultado de la division
    '''
    if divisor == 0:
        return False
    resultado = dividendo / divisor
    return resultado


# 4.3 
def calcular_promedio(lista:list, dato:str)->float:
    '''
    Brief:
    - Calcula el promedio de los valores numéricos de una clave específica en los diccionarios que representan a los heroes en una lista.

    Param:
    - lista: Una lista de superhéroes representados como diccionarios.
    - dato: Un string que especifica la clave sobre la que se calculará el promedio.

    Return:
    - El promedio de los valores numericos de la clave especificada en los diccionarios de la lista. 
    - Si no se encuentran valores numericos en la clave o si la lista está vacia, la función devuelve `False` para indicar un error o falta de datos.
    '''
    suma = sumar_dato_heroe(lista, dato)
    contador = len(lista)
    
    if contador == 0:
        return False
    
    promedio = dividir(suma, contador)
    return promedio


# 4.4 
def mostrar_promedio_dato(lista:list, dato:str)->str:
    '''
    Brief:
    - Esta funcion muestra el promedio de un dato específico en una lista de heroes.
    Param:
    - lista: Una lista de heroes representados como diccionarios. 
    - dato: Un string que especifica el nombre del dato del que se desea calcular el promedio.
    Return:
    - Si la lista está vacia o si alguno de los heroes no tiene un valor numérico para el dato especificado, la función devuelve `False` para indicar un error o falta de datos.
    - Si la lista contiene datos validos, la funcion calcula y muestra el promedio del dato especificado por consola.
    '''
    if len(lista) == 0:
        return False
    for heroe in lista:
        if type(heroe[dato]) != int and type(heroe[dato]) != float:
            return False
    promedio = calcular_promedio(lista, dato)

    print(f"Promedio de {dato}: {promedio}")


# 5.1 
def imprimir_menu(menu):
    '''
    Brief:
    - Esta funcion imprime un menú en la consola. Cada opción del menú se proporciona como una lista de cadenas.
    Param:
    - menu: Una lista de cadenas que representan las opciones del menú que se desea imprimir.
    Return:
    - La función no devuelve nada simplemente imprime el menú en la consola.
    '''
    for opcion in menu:
        print(opcion)


# 5.2 
def validar_entero(numero_string:str):
    '''
    Brief:
    - Esta funcion valida si una cadena es un numero entero valido.
    Param:
    - numero_string: Una cadena que se desea validar como número entero.
    Return:
    - True si la cadena representa un número entero válido, False en caso contrario.
    '''
    if numero_string.isdigit():
        return True
    else:
        return False


# 5.3 
def stark_menu_principal(menu)->int:
    '''
    Brief:
    - Recibe una opcion ingresada por el usuario, la valida como un numero entero y se asegura que este dentro del rango elegido.
    Param:
    - menu: Una lista de opciones de menú representadas como cadenas.
    Return:
    - El numero de opcion elegida por el usuario si es un numero entero valido y esta dentro del rango de opciones del menu.
    - False si la opcion ingresada por el usuario no es válida.
    '''
    imprimir_menu(menu)
    opcion_elegida = input("Ingrese una opcion: ")
    validacion = validar_entero(opcion_elegida)
    if validacion == True:
        numero_casteado = int(opcion_elegida)
        if numero_casteado > 0 and numero_casteado < 13:
            return numero_casteado
    else:
        return False


# MENU
def mostrar_nombres_nb(lista:list)->str:
    '''
    Brief:
    - Muestra por terminal todos los nombres del genero "NB" que se encuentren en una lista
    Param:
    - lista: La lista de donde debe iterar en busca de los nombres
    Return: 
    - No tiene return
    '''
    for heroe in lista:
        if heroe["genero"] == "NB":
            obtener_nombre(heroe)

# Opcion 3 y 4
def heroe_mas_alto(lista:list, genero:str)->str:
    '''
    Brief:
    - Muestra por terminal el heroe mas alto (dependiendo de su genero) que este en la lista
    Param:
    - lista: La lista de donde debe iterar para encontrar al mas alto dependiendo de su genero
    - genero: Dependiendo de cual se elija (M, F o NB) tomara a diferentes heroes   
    Return:
    - Devuelve una lista con el nombre del heroe mas alto del genero elegido
    '''
    heroes_del_mismo_genero = []
    for heroe in lista:
        if heroe["genero"] == genero:
            heroes_del_mismo_genero.append(heroe)

    heroes_altos = obtener_dato_cantidad(heroes_del_mismo_genero, "maximo", "altura")
    stark_imprimir_heroes(heroes_altos)

# Opcion 5 y 6
def heroe_mas_debil(lista:list, genero:str)->str:
    '''
    Brief:
    - Muestra por terminal el heroe mas debil (dependiendo de su genero) que este en la lista
    Param:
    - lista: La lista de donde debe iterar para encontrar al mas debil dependiendo de su genero
    - genero: Dependiendo de cual se elija (M, F o NB) tomara a diferentes heroes   
    Return: 
    - Devuelve una lista con el nombre del heroe mas debil del genero elegido
    '''
    heroes_del_mismo_genero = []
    for heroe in lista:
        if heroe["genero"] == genero:
            heroes_del_mismo_genero.append(heroe)

    heroes_debiles = obtener_dato_cantidad(heroes_del_mismo_genero, "minimo", "fuerza")
    stark_imprimir_heroes(heroes_debiles)

# Opcion 7
def fuerza_promedio(lista:list, genero:str, dato:str)->float:
    '''
    Brief:
    - Muestra por terminal el promedio de fuerzaz de los heroes del genero que se elija.
    Param:
    - lista: La lista de donde debe iterar para encontrar la fuerza de los heroes del genero que se elija.
    Return: 
    - Devuelve al promedio de fuerza del genero en cuestion por consola.
    '''
    heroes_del_mismo_genero = []
    for heroe in lista:
        if heroe["genero"] == genero:
            heroes_del_mismo_genero.append(heroe)

    mostrar_promedio_dato(heroes_del_mismo_genero, dato)

# Opcion 8 y 9
def mostrar_cantidad_tipos(lista:list, tipo:str)->dict:
    '''
    Brief:
    - Determina cuantos heroes hay con cada tipo de color de ojos o pelo.
    Param:
    - lista: La lista de donde debe iterar para encontrar los tipos de color de ojos o de pelo de los heroes
    - tipo: key de diccionario para determinar si la funcion contara los tipos de color de ojos o de pelo
    Return:
    - Devuelve un diccionario con la suma de cada tipo de color de ojos o de pelo
    '''
    conteo_color = {}
    for heroe in lista:
        caracteristica = heroe[tipo].lower()
        if caracteristica and caracteristica != "no hair":
            if caracteristica in conteo_color:
                conteo_color[caracteristica] += 1
            else:
                conteo_color[caracteristica] = 1
    return conteo_color

# Opcion 10 y 11
def mostrar_heroes_agrupados(lista:list, tipo:str)->dict:
    '''
    Brief:
    - Agrupa a todos los heroes dependiendo de su color de ojos o de su tipo de inteligencia
    Param:
    - lista: La lista de donde debe iterar para encontrar los colores de ojos o el tipo de inteligencia
    - tipo: key de diccionario para determinar si la funcion agrupara por colores de ojos o por tipos de inteligencia
    Return:
    - Devuelve un diccionario con los heroes agrupados en su respectivo color o tipo de inteligencia 
    '''
    heroes_por_caracteristicas = {}
    for heroe in lista:
        caracteristica = heroe[tipo].lower()
        if caracteristica:
            if caracteristica in heroes_por_caracteristicas:
                heroes_por_caracteristicas[caracteristica].append(heroe["nombre"])
            else:
                heroes_por_caracteristicas[caracteristica] = [heroe["nombre"]]
    return heroes_por_caracteristicas
def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print("Palabra: " + str(palabra))
    longitud = len(palabra)
    print("Longitud: " + str(longitud))
    primera = palabra[0]
    print("Primera letra: " + str(primera))
    ultima = palabra[-1]
    print("Ultima letra: " + str(ultima))
    repetida = (palabra*(3))
    print("Repetida: " + str(repetida))
    decorada = ("***" + str(palabra) + "***")
    print("Decorada: " + str(decorada))
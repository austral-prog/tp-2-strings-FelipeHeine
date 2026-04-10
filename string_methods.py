from gettext import find


def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    print("Strip: " + str(nombre.strip()))
    print("Lstrip: " + str(nombre.lstrip()))
    print("Rstrip: " + str(nombre.rstrip()))
    print("Upper: " + str(frase.upper()))
    print("Lower: " + str(frase.lower()))
    print("Title: " + str(frase.title()))
    print("Find: " + str(frase.find("gran")))
    print("Replace: " + str(frase.replace("programacion","desarrollo")))
    print("Count: " + str(frase.count("a")))
    print("Contiene Python: " + str("Python" in frase))
    print("Contiene Java: " + str("Java" in frase))
    print("Slice: " + str(frase[0:6]))
    print("Paso: " + str("Python"[::2]))
    print("Reverso: " + str("Python"[::-1]))
    print("Formato: " + (str(nombre).strip() + " " + "sabe " + str(frase[0:6])))
    print(multilinea)
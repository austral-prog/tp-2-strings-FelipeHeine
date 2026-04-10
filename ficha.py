from http.cookiejar import uppercase_escaped_char


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)


    nombre = input("Nombre completo:").strip().lower()
    email = input("ingresa Mail: ")
    nota = int(input("ingresa nota 1: "))
    nota2 = int(input("ingresa nota 2: "))
    nota3 = int(input("ingresa nota 3: "))
    print( """========================
    FICHA DEL ALUMNO
========================""")
    print("Nombre: " + str(nombre.title()))
    print("Email: " + str(email.lower()))
    print("Caracteres en nombre: " + str(len(nombre)))
    print("Iniciales:", f"{nombre[0].upper()}{nombre[nombre.find(" ")+1].upper()}", )
    print("Usuario:", f"{(nombre[nombre.find(" ")+1:]).lower()}.{(nombre[0:nombre.find(" ")]).lower()}")
    print("Email valido:" , str("@" in email))
    print("Dominio: " + f"{email[email.find("@")+1:].lower()}")
    print("Nombre para archivo: " + str(nombre.replace(" ","_").title()))
    print("Cantidad de a: " + str(nombre.count("a")))
    print("Codigo secreto: " + str(nombre[::-1].upper()))
    print("Nota 1: " + str(nota))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    print("Suma: " + str(nota + nota2 + nota3))
    print("Promedio: " + str((nota + nota2 + nota3)/3))
    print("Promedio entero: " + str(round((nota + nota2 + nota3) /3)))
    cierre = "=" * 24
    print(cierre)
ficha()
from http.cookiejar import uppercase_escaped_char

def ficha():
    """
    Ejercicio integrador.
    """

    nombre = input("Nombre completo: ").strip().title()
    email = input("Ingresa mail: ").lower()

    nota1 = int(input("Ingresa nota 1: "))
    nota2 = int(input("Ingresa nota 2: "))
    nota3 = int(input("Ingresa nota 3: "))

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")

    print("Nombre:", nombre)
    print("Email:", email)

    print("Caracteres en nombre:", len(nombre))

    print(f"Iniciales: {nombre[0]}{nombre[nombre.find(' ') + 1]}")

    print(
        f"Usuario: {nombre[nombre.find(' ') + 1:].lower()}."
        f"{nombre[:nombre.find(' ')].lower()}"
    )

    print("Email valido:", "@" in email)

    print("Dominio:", email[email.find("@") + 1:])

    print("Nombre para archivo:", nombre.replace(" ", "_"))

    print("Cantidad de a:", nombre.lower().count("a"))

    print("Codigo secreto:", nombre[::-1].upper())

    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Nota 3:", nota3)

    suma = nota1 + nota2 + nota3

    print("Suma:", suma)
    print("Promedio:", suma / 3)
    print("Promedio entero:", suma // 3)

    print("=" * 24)
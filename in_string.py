def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("escriba un nombre: ").lower()

    print("Contiene a: " + str("a" in nombre))
    print("Contiene e: " + str("e" in nombre))
    print("Contiene i: " + str("i" in nombre))
    print("Contiene o: " + str("o" in nombre))
    print("Contiene u: " + str("u" in nombre))

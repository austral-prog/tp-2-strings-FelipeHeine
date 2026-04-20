from ctypes.macholib.dylib import dylib_info


def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto = float(input("Ingresar gasto: "))
    recibido = int(input("Ingrese el dinero recibido: "))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(recibido)
    print("")
    print("Vuelto")
    print("")
    (vuelto) = int(recibido) - float(gasto)
    pesos = int(vuelto)
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    centavos = round((vuelto - pesos)*100)
    print(centavos)



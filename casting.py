from http.client import CannotSendRequest
from multiprocessing.spawn import prepare
def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    cantidad = float(input("Cantidad: "))
    precio_descuento = (precio - descuento)
    total = (precio_descuento * cantidad)

    print( f'Precio: {precio}' )
    print( f'Descuento: {descuento}' )
    print( f'Precio con descuento: {precio_descuento}')
    print( f'Total: {total}')
casting()

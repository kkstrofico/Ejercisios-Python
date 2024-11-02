from boletas import almacenamiento_documento
#Evita que se ingrese un documento ya existente
def evitar_documento_repedito(documento):
    while documento in almacenamiento_documento:
        print('\nError el documento ingresado ya existe')
        documento = input('Ingresa el documento nuevamente: ')
    return documento
#Evita que se compren mas de 4 boletas
def cantidad_boletas_4(cantidad):
    while cantidad > 4:
        print('\nNo se pueden comprar mas de cuatro boletas')
        cantidad = int(input('Ingresa una cantidad menor que 4: '))
    return cantidad
#Evita que la cantiad de boletas supere la cantidad disponible
def superar_cantidad(cantidad,cantidad_disponible):
    while cantidad > cantidad_disponible:
        print(f'Ingresa una cantidad menor o igual que: {cantidad_disponible}')
        cantidad = int(input('Ingresa nuevamente la cantidad: '))
    return cantidad
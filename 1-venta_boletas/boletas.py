cantidad_boletas = 10
almacenamiento_documento = []
def comprar_boleta(documento,cantidad_boletas_compradas,cantidad_actual):
    almacenamiento_documento.append(documento)
    cantidad_actual -= cantidad_boletas_compradas
    return cantidad_actual
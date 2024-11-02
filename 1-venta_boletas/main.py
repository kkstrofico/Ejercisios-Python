from boletas import *
from utils import evitar_documento_repedito,cantidad_boletas_4,superar_cantidad
""" 
Diseñe un algoritmo para organizar la venta de boletas en línea para el ingreso a un concierto,
cada persona que desee ingresar debe presentar su cédula de ciudadanía,
el algoritmo debe leer y agregar a un vector el número del documento de identidad.
En el caso de que la identificación ya exista en el vector, 
debe mostrar un mensaje que rechace la venta de la boleta, en el momento que la venta se realice, 
el algoritmo debe permitir que lea la cantidad total de boletas que se compra 
(no mayor a 4) y reste de la cantidad disponible, 
cuando esta cantidad llegue a cero, muestre un mensaje y finalice.

--Analisis--
Requisitos
-Cada persona que ingrese debe presentar su cedula de ciudadania.
-Se debe agregar la cedela de cidadania a un vector
-Mostrar mensaje de error en caso de que la el documento ya este en el vector
-Se debe permitir la lectura de cantidad de boletas que se compra(No mayor a 4)
-Se debe tener una cantidad de boletas disponible
-Finalice el programa cuando se acaben las boletas mostrando un mesaje

Entrada
-Cedula
-Cantidad Voletas


Proceso 
1.Solicita el numero de documento de identidad
2.Si el documento no se encuetra registrado pregunto la cantidad de boletas que desea llevar
3.Resto la cantidad de boletas compradas a la cantidad de boletas disponibles


Salida 
4.Muestro mensaje de exito
"""
if __name__ == '__main__':
    #Solicitamos los datos
    while cantidad_boletas != 0:
        try:
            numero_documento = evitar_documento_repedito(input('DOCUEMENTO: '))
            cantidad_compradas = cantidad_boletas_4(int(input('CANTIDAD: ')))
            cantidad_compradas = superar_cantidad(cantidad_compradas,cantidad_boletas)
            cantidad_boletas = comprar_boleta(numero_documento,cantidad_compradas,cantidad_boletas)
            print(cantidad_boletas,almacenamiento_documento)
        except ValueError:
            print('Upps a ocurrido un error')


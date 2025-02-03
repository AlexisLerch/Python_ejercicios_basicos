# 1- Crear un diccionario y mostrar si esta la palabra pedida dentro del mismo
"""divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

usuario = input('Ingrese una divisa: ')

print(divisa.get(usuario.title(), "La divisa no esta."))

if usuario.title() in divisa:
    print(divisa[usuario.title()])
else:
    print("La divisa no esta.")"""



# 2- Preguntar al usuario nombre, edad, direccion y telefono y lo guarde y despues mostrarlo
"""nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
direccion = input('Ingrese su direccion: ')
telefono = input('Ingrese su telefono: ')
usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono,
    }
print(usuario['nombre'], 'tiene', usuario['edad'], 'años, vive en', usuario['direccion'], 'y su numero de telefono es', usuario['telefono'])
#print(f'{usuario['nombre']} tiene {edad} años, vive en {direccion} y su numero de telefono es {telefono}')"""



# 3- Guardar un diccionario de precios donde el usuario pregunta por una fruta y kg y muestre el precio
"""frutas = {
    'banana': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70,
    }

fruta = input('Ingrese una fruta: ')
kilo = float(input('Ingrese los kilos: '))
total = 0

if fruta in frutas:
    print(kilo, 'kilos de', fruta, 'valen', round(frutas[fruta]*kilo, 2), '$')
else:
    print('Lo sentimos, la fruta', fruta, 'no esta disponible')"""



# 4- Pregunta frecha y muestra la misma fecha
"""meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio',
         7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Ingrese una fecha formato dd/mm/aaaa: ')
print(fecha)
fecha = fecha.split('/')
print(fecha)
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])"""



# 5- Almacen de asignaturas
"""curso =  {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0

for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'creditos')
    total_creditos += creditos
print('Total de creditos: ', total_creditos)"""



# 6- While creando un diccionario
"""persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "si"""



# 7- Agregar compras y al final mostrar el total
"""compras = {}
continuar = True
total = 0
while continuar:
    articulo = input('Ingrese el articulo: ')
    precio = int(input('El precio de ' + articulo + ' es: '))
    compras[articulo] = precio
    total += precio
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "si"

print('Lista de compra')
for articulo, precio in compras.items():
    print(articulo, '\t', precio)
print('Total:', total)"""




























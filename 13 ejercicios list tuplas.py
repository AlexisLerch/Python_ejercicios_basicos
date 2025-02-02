# Crear lista y mostrar en pantalla
"""lista = ['matematica', 'fisica', 'historia']
print(lista)"""


# Mostrar elementos de una lista
"""lista = ['matematica', 'fisica', 'historia']
for materia in lista:
    print(f'Yo estudio {materia}')"""



# Agregar notas en una nueva lista y mostrar la nota con su materia
"""lista = ['matematica', 'fisica', 'historia']
notas = []

for materia in lista:
    nota = input(f'ingrese la nota que saco en {materia}: ')
    notas.append(nota)
for i in range(len(lista)):
    print(f'En {lista[i]} has sacado {notas[i]}')"""



# Lista de numeros y ordenarla de mayor a menor
"""numeros = []
for i in range(6):
    num = int(input('Ingresa los numeros ganadores: '))
    numeros.append(num)
numeros.sort()
print(numeros)"""



# Ordenar una lista
"""lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in range(1,11):
    print(lista[-num], end=", ")"""



# Eliminar de una lista
"""lista = ['matematica', 'fisica', 'historia']
aprobado = []
for materia in lista:
    nota = int(input(f'ingrese la nota de {materia}'))
    if nota > 6:
        aprobado.append(materia)
for materia in aprobado:
    lista.remove(materia)
print(lista)"""



# Abecedario eliminando multiplos de 3
"""abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for letra in range(len(abc), 1, -1):
    if letra % 3 == 0:
        abc.pop(letra - 1)
print(abc)"""



# Palindromo
"""def es_palindromo(palabra):
    palabra = palabra.lower().replace(' ', '')
    return palabra == palabra[::-1]

palabra = input('Ingrese una palabra: ')
if es_palindromo(palabra):
    print('si')
else:
    print('no')"""


"""def es_palindromo(palabra):
    nueva_palabra = ''
    for letra in palabra:
        if letra != " ":
            if 'A' <= letra <= 'Z':
                nueva_palabra += chr(ord(letra) + 32)
            else:
                nueva_palabra += letra

    izquierda = 0
    derecha = len(nueva_palabra) - 1

    while izquierda < derecha:
        if nueva_palabra[izquierda] != nueva_palabra[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True

palabra = input('Ingrese una palabra: ')
if es_palindromo(palabra):
    print(f'{palabra} es palindromo')
else:
    print(f'{palabra} no es palindromo')"""



# Pedir palabra al usuario y mostrar cuantas veces contiene cada vocal
"""palabra = input('Ingrese una palabra: ')
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    cantidad = 0
    for letra in palabra:
        if letra == vocal:
            cantidad += 1
    print(f'La vocal {vocal} aparece: {cantidad} veces.')"""



# Almacenar precios y mostrarlos ordenados
"""precios = [50, 75, 46, 22, 80, 65, 8]
precio_minimo = precios[0]
precio_maximo = precios[0]

for precio in precios:
    if precio < precio_minimo:
        precio_minimo = precio
    if precio > precio_maximo:
        precio_maximo = precio

print(precio_minimo)
print(precio_maximo)"""



# Producto escalar
"""v1 = [1, 2, 3]
v2 = [-1, 0, 2]
producto_escalar = 0
for i in range(len(v1)):
    producto_escalar += v1[i] * v2[i]

print(f'{v1} x {v2} = {producto_escalar}')"""



# Listas anidadas producto de una matris
"""a = ((1, 2, 3), (4, 5, 6))
b = ((-1, 0), (0, 1), (1, 1))
result = [[0, 0], [0, 0]]
print(a,b)

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])"""



# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica
"""sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)"""




























































































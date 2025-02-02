# Pedimos que ingrese un numero para calcular la suma de todos los numeros
num = int(input("ingresa un numero: "))

# Creamos la lista en un rango de 1 hasta n + 1, que seria en este caso 10
# el + 1 es porque empezamos desde el 1 y no del 0, incluimos el 10
lista = list(range(1, num + 1))

resultado = sum(lista)

print(resultado)

# Crear una funcion que devuelva el cuadrado de un numero.
def cuadrado(n):
    return n ** 2
    #n = n ** 2
    #print(n)
    

n = int(input("ingrese un numero para calcular el cuadrado: "))

print(cuadrado(n))


# Crear un Diccionario.

herramientas = {"lenguaje":"Python",
                "a":"b",
                "c":"d",}
print(f'{herramientas}')


# Verificar si un numero es positivo negativo o cero.

num = int(input('ingrese un numero: '))

if num > 0:
    print('positivo')
elif num < 0:
    print('negativo')
else:
    print('cero')

# Lista de numeros pares de 1 al 20

# Creamos lista vacia.
lista_numeros_pares = []

# Recorremos cada numero del rango dado, y decimos solo agregar a la lista
# si el modulo o resto de dividir el numero en dos da cero, ej 2/4=0 o 4/4=0 hablando
# del resto es cero y lo agregamos a la lista

for numero in range(1, 21):
    if numero % 2 == 0:
        lista_numeros_pares.append(numero)

print(lista_numeros_pares)

# 6 Calcular el factorial de un numero usando while

numero = int(input('Ingrese un numero para saber su factorial: '))
factorial = 1
i = 1

while i <= numero:
    factorial *= i
    i += 1

print(f'{factorial}')


# 7 invertir cadena de texto en bucle

cadena = input('ingrese un texto')
cadena_reversa = ''

for letra in cadena:
    cadena_reversa = letra + cadena_reversa

print(f'{cadena_reversa}')


# 8 Contar vocales de un texto

vocales = 'aeiouAEIOU'
count = 0
texto = input('Ingrese un texto: ')
for letra in texto:
    if letra in vocales:
        count += 1
    #return count

print(f'{count}')


# 9 Encontrar el maximo en una lista

lista = [1000, 10, 1, 5, 35]
maximo = lista[0]

for num in lista:
    if num > maximo:
        maximo = num
        
print(maximo)

# Estrellas.
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print('')

for i in range(n, 0, - 1):
    print('*' * i)

for i in range(n):
    espacios = ' ' * (n - i - 1)
    estrellas = '*' * (2 * i + 1)
    print(espacios + estrellas)

# Lista con los primeros 10 numeros al cuadrado.

lista_cuadrados = []

for i in range(1,11):
    lista_cuadrados.append(i ** 2)

print(lista_cuadrados)


# Encontrar la suma de todos los impares hasta 50.

suma_impares = 0

for i in range(1,51):
    if i % 2 != 0:
        suma_impares += i
print(suma_impares)

# Fibonacci
n = 10
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(fib)

# Fibonacci 2

n1, n2 = 0, 1
for i in range(10):
    print(n1, end=", ")

    num = n1 + n2
    n1 = n2
    n2 = num
    #print(n1)

# Polindrome
cadena = input('ingresa un texto: ')
reversa = cadena[::-1]

if cadena.lower() == reversa.lower():
    print('es polindromo')
else:
    print('no es polindromo')


# Encontrar longitud de la palabra mas larga en una lista
palabras = ['Encontrar','longitud','mas','polindromo']
palabra_larga = max(palabras, key=len)
longitud_max = len(palabras[0])
for palabra in palabras[1:]:
    longitud_actual = len(palabra)
    if longitud_actual > longitud_max:
        longitud_max = longitud_actual
print(f'la palabra mas larga es: {palabra_larga} cantidad de letras es: {longitud_max}')


# Cantidad de veces que aparece una letra en un texto"
texto = 'Alexis Lerch'
conteo = {}

for letra in texto.lower():
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1
print(conteo)

# TresCinco

for numero in range(1, 31):
    if numero % 3 == 0 and numero % 5 == 0:
        print('TresCinco')
    elif numero % 3 == 0:
        print('Tres')
    elif numero % 5 == 0:
        print('cinco')
    else:
        print(numero)
 
        
# Imprimir tabla 1 al 5
for i in range(1, 6):
    for j in range(1, 6):
        print(f'{i} x {j} = {i * j}', end="     ")
    print("")


# Segundo numero mas grande en una lista
lista_numeros = [10, 20, 5, 30, 45, 11]
#lista_numeros.sort()

#print(lista_numeros[-2])
maximo = segundo_maximo = lista_numeros[0]

for numero in lista_numeros[1:]:
    if numero > maximo:
        segundo_maximo = maximo
        maximo = numero
    elif numero > segundo_maximo and numero != maximo:
        segundo_maximo = numero
print(maximo)
    



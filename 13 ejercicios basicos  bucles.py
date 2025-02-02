# PALABRA POR 10
"""palabra = input('Ingrese una palabra y se repetira 10 veces: ')
for i in range(10):
    print(palabra)"""




# EDAD DICIENDO CUANTAS VECES CUMPLIO
"""edad = int(input('Ingrese su edad: '))
for i in range(0, edad):
    print('usted a cumplido ', i + 1)"""




# NUMEROS IMPARES          
"""numero = int(input('ingrese un numero: '))
for i in range(numero):
    if i % 2 !=0:
        print(i, end=", ")"""
    



# NUMERO POSITIVO CUENTA ATRAS
"""numero = int(input('Ingrese un numero: '))
for i in range(numero, -1, -1):
    print(i, end=", ")"""




# INVERSION COMPUESTA
"""invertir = int(input('Ingrede la cantidad a invertir: '))
interes = int(input('Ingrese el interes anual: '))
años = int(input('Ingrese el total de años: '))

for i in range(años):
    invertir *= 1 + interes / 100
    print('Capital tras ' + str(i+1) + ' años: ' + str(round(invertir, 2)))"""




# PIRAMIDE DE ESTRELLAS
"""numero = int(input('Ingrese un numero: '))
for i in range(numero):
    for j in range(i+1):
        print('*', end=' ')
    print('')

for i in range(numero, -1 ,-1):
    print('* '*(i+1))"""




# TABLAS
"""for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}', end="\t")
    print('')"""



# NUMEROS IMPARES EN PIRAMIDE
"""numero = int(input('Ingrese un numero: '))
for i in range(1, numero + 1, 2):
    for j in range(i, 0, - 1):
        if j % 2 != 0:
            print(j, end=' ')
    print('')"""




# COMPROBAR CONTRASEÑA HASTA QUE SEA LA CORRECTA.
"""contraseña = 'python2025'
contraseña_ingresada = ''

while contraseña != contraseña_ingresada:
    contraseña_ingresada = input('ingrese la contraseña: ')
print('Contraseña correcta, ingresando... ')"""




# PRIMOS.
"""n = int(input('ingrese un numero mayor a 1: '))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print('es primo')
else:
    print('no es primo')

es_primo = True
if n <= 1:
    es_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
if es_primo:
    print('primo')
else:
    print('No primo')"""




# INGRESAR PALABRA Y MOSTAR LETRAS UNA POR UNA DESDE LA ULTIMA
"""palabra = 
reverso = ''
for letra in range(len(palabra) -1, -1, -1):
    #reverso = letra + reverso
    print(palabra[letra])
print(reverso)"""




# INGRESA UNA PALABRA Y UNA LETRA MUESTA LAS VECES QUE APARECE LA LETRA EN LA FRASE
"""frase = input('Ingrese una palabra: ')
letra = input('Ingrese una letra: ')
#lista = []
count = 0
for i in frase:
    if i == letra:
        #lista.append(i)
        count += 1
print(f'La letra {letra} aparece: {count} veces en la frase')"""




# PODER ESCRIBIR HASTA QUE EL USUARIO ESCRIBE SALIR
"""while True:
    frase = input('ingrese una frase: ')
    if frase == 'salir':
        break
    print(frase)"""
    




























































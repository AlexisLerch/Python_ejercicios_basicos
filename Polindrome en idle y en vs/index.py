def es_palindromo(palabra):
    # Primer letra 
    primera = 0
    
    # Ultima letra
    ultima = len(palabra) - 1
    
    # Comparar las primera (a) y la ultima (b) letras en un for
    for i in range(0, len(palabra)):
        # si la ultima y primer letra son iguales sumamos 1 y continua el for con la segunda letra y la ante ultima y asi sucesivamente 
        if palabra[primera] == palabra[ultima]:
            primera += 1
            ultima -= 1
        # sino retorna false osea que si no son iguales alguna letra en la comparacion, no es polindrome
        else:
            return False

    return True
    
palabra = input("Ingrese una palabra: ")

if es_palindromo(palabra):
    print("es palindrome")
else:
    print("no es palindrome")
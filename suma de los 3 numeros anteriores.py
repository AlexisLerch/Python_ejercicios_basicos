def encontrar_ultimos_digitos():
    a, b, c = 2023, 2024, 2025
    diccionario = {}
    for i in range(1, 2023202320232023 + 1): # +1 porque empezamos desde 1
        siguiente = (a + b + c) % 10000
        if (a % 10000, b % 10000, c % 10000) in diccionario:
            ciclo_inicio = diccionario[(a % 10000, b % 10000, c % 10000)]
            longitud_ciclo = i - ciclo_inicio
            posicion_relativa = (2023202320232023 - ciclo_inicio) % longitud_ciclo
            return list(diccionario.keys())[list(diccionario.values()).index(ciclo_inicio + posicion_relativa)][2]
        diccionario[(a % 10000, b % 10000, c % 10000)] = i
        a, b, c = b, c, siguiente
        return c # Si no hay ciclo, pero esto es muy improbable con un número tan grande
resultado = encontrar_ultimos_digitos()
print(f"Los últimos 4 dígitos del número en la posición 2023202320232023 son: {resultado}")

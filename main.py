def cadenas_repetidas(c):
    frecuencia = {}                        #Diccionario para almacenar la frecuencia
    result = {}                            #Diccionario para almacenar las subcadenas repetidas y sus numero

    # Itera a través de la cadena para encontrar todas las subcadenas posibles de longitud 4
    for i in range(len(c) - 3):
        sub = c[i:i+4]                     #Extrae la subcadena de longitud 4
        if sub in frecuencia:
            frecuencia[sub] += 1           #Si la subcadena ya está en el diccionario, incrementa su frecuencia
        else:
            frecuencia[sub] = 1            #Si la subcadena no está en el diccionario, inicializa su frecuencia en 1

    # Itera a través del diccionario de frecuencia para encontrar las subcadenas repetidas
    for sub, count in frecuencia.items():
        if count > 1:                      #Si la frecuencia de una subcadena es mayor que 1, significa que aparece más de una vez
            result[sub] = count            #Almacena la subcadena y su frecuencia en el diccionario de resultados

    return result                          #Devuelve el diccionario que contiene las subcadenas repetidas y su numero de ocurrencias


# Al tener dos bucles separados, la complejidad general de la solución es lineal
# es decir, O(2n) -> O(n)

if __name__ == "__main__":
    cadena = "abcdefghijklmnpqrsabcdabcdfghijklmefgheabcdtuvwxyzfghabcfghijklmnopqfgherstabcdefgtrijklmnopqrsfghtrijklmnopqrstabcdrstuvwxyzabcd"
    resultado = cadenas_repetidas(cadena)
    print(resultado)

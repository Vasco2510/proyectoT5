


"""
Gonzalo desea calcular la suma dc los dígitos del factorial dc un número considerando
que solo sumará los dígitos impares del factorial del número.
Realice una función que reciba como parámetro un número n y la función devuelva
la suma de los dígitos del factorial de un número n considerando que cuando el dígito
Es par el valor a sumar es 0, en caso contrario se suma el valor del dígito correspondiente .
"""

def myfuntion(n):
    factorial = 1
    suma = 0

    i=1
    while i<=n:
        factorial = factorial*i
        i = i+1
    result = factorial
    while factorial>0:
        cifra = factorial%10
        factorial = factorial//10

        if cifra % 2 != 0:
            suma = suma + cifra

    return suma, result

n = int(input("Ingrese un numero a obtener su factorial"))
result1, result2 = myfuntion(n)

print("la suma de cifras es: ", result1, " y el factorial era ", result2)
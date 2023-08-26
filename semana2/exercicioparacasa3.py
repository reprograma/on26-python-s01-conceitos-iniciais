def calcular_soma(a, b, c):
    soma = a + b + c
    return soma

num1 = float(input('digite o primeiro número: '))
num2 = float(input('digite o segundo número: '))
num3 = float(input('digite o terceiro número: '))

resultado = calcular_soma(num1, num2, num3)
print(f'a soma dos três números é: {resultado}')
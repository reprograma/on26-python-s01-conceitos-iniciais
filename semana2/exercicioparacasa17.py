import math

area = float(input('digite o tamanho em metro quadrado de area a ser pintada: '))
litros = area/6
litros_com_folga = litros * 1.1

lata = int(litros_com_folga/18)
resto = litros_com_folga % 18
galoes = math.ceil(resto/3.6)
preco = (lata * 80) + (galoes * 25)

print(f'misture latas e galoes')
print(f'voce precisa de {lata} latas e galoes {galoes} galoes de tinta')
print(f'o preco total é de R$ {preco:.2f}')

# 16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

cobertura_por_litro = 3  # metros quadrados
capacidade_lata = 18  # litros
preco_lata = 80.00  # em reais

def calcular_tinta(area):
    litros_necessarios = area / cobertura_por_litro
    latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)
    preco_total = latas_necessarias * preco_lata
    return latas_necessarias, preco_total

area_a_pintar = float(input('digite o tamanho em metros quadrados da área a ser pintada: '))

latas, preco_total = calcular_tinta(area_a_pintar)
print(f'quantidade de latas necessárias: {latas}')
print(f'preco total: R$ {preco_total:.2f}')

# Bibliotecas importadas:
import math

# Inteiro
# 1) Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1_1 = int(input("insira um numero inteiro: "))
numero_1_2 = int(input("insira um numero inteiro: "))
resultado_1 = numero_1_1 + numero_1_2
print("Exercicio 1 :",resultado_1)

# 2) Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_2_1 = int(input("insira um numero inteiro: "))
resultado_2 = numero_2_1 % 5
print(f"Exercicio 2: O resto da divisão por 5 é: {resultado_2}")

# 3) Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_3_1 = int(input("Digito um numero: "))
numero_3_2 = int(input("Digito um numero: "))
resultado_3 = numero_3_1 * numero_3_2
print("Exercicio 3:", resultado_3)

# 4) Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_4_1 = int(input("insira um numero inteiro: "))
numero_4_2 = int(input("insira um numero inteiro: "))
resultado_4 = numero_4_1 // numero_4_2
print("Exercicio 4:", resultado_4)

# 5) Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_5_1 = int(input("Digite um numero: "))
resultado_5 = numero_5_1 ** 2
print ("Exercicio 5 :", resultado_5)

#Números de Ponto Flutuante (float)

# 6) Escreva um programa que receba dois números flutuantes e realize sua adição.
num_6_1 = float(input("Digite numero: "))
num_6_2 = float(input("Digite numero: "))
resultado_num6 = num_6_1 + num_6_2
print ( "Exercicio 6: A soma é:", resultado_num6)

# 7) Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_7_1 = float(input("Digite um numero: "))
num_7_2 = float(input("Digite um numero: "))
resultado_7 = (num_7_1 + num_7_2) / 2
print (("Exercicio 7: A media ", resultado_7))

# 8) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base **expoente
print ("Exercicio 8, a pontência é:", potencia)

# 9) Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temparatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32 #Formula é multiplica a temperatura por 1,8 e soma a 32
print(f"Exercicio 9: {celsius}°C é igual a {fahrenheit}°F")

# 10) Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo **2
print (f"Exercicio 9:{area_do_circulo:.3f}")


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
print (f"Exercicio 10:{area_do_circulo:.3f}")

# Strings (str)

# 11) Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")
texto_maisculo = texto.upper()
print("Ex. 11 = Texto em maiúsculo: ", texto_maisculo)

# 12) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_usuario = input("Digite o seu nome completo: ")
nome_minusculo = nome_usuario.lower()
print("Ex.12 = Nome em minusculo é: ", nome_minusculo)

# 13) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase_1 = input("Escreva um frase: ")
frase_sem_espaco = frase_1.strip()
print("Ex.13 = Frase sem espaço no inicio e fim:", frase_sem_espaco)

# 14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_de_dia_mes_ano = data_usuario.split("/")
print(f"o elemento 1 do ex. 14 é o: {lista_de_dia_mes_ano[0]}")
print(f"o elemento 1 do ex. 14 é o: {lista_de_dia_mes_ano[1]}")
print(f"o elemento 1 do ex. 14 é o: {lista_de_dia_mes_ano[2]}")

# 15) Escreva um programa que concatene duas strings fornecidas pelo usuário.
palavra_1 = input("Digita um palavras: ")
palavra_2 = input("Digita a segunda palavra")
texto_concatene = palavra_1 + palavra_2
print("Ex.15 =  Texto junto é", texto_concatene)

#Booleanos (bool)
# 16) Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = input("Escreva a palavra True ou False: ")
valor2 = input("Escreva a palavra True ou False: ")
resultado_and = valor1 and valor2
print("Ex. 16 Resultado and: ", resultado_and)

# 17) Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
resultado_or = valor1 or valor2
print("Ex.17 Resultado or: ", resultado_or)

# 18) Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor
valor_3 = input("Escreva um valor booleano: False/True: ")
resultado_not = not valor_3
print("Ex.18 resultado do valor not é", valor_3)

# 19) Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
valor_4 = float(input("Valor: "))
valor_5 = float(input("Valor: "))
resultado_igualdade = valor_4 == valor_5
print("Ex.19 =  Resultado da igualdade é:", resultado_igualdade)

# 20) Escreva um programa que verifique se dois números f
resultado_diferente = (valor_4 != valor_5)
print("Ex. 20 o resultado da diferença é:", resultado_diferente)

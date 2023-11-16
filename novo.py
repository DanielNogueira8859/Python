import random

#contador = 1
# while contador <= 5:
#     print ("numero",contador)
#     contador = contador +1


# contador = 10
# while contador > 0:
#     print(contador)
#     contador = -1
#     print(contador)

# tentativas = 3
# senha = "oi"

# while tentativas > 0:
#     senhaInserida = input("Digite a senha:  ")
#     if senhaInserida == senha:
#         print("Senha correta")
#         break
#     else:
#         print("Senha incorreta")
#         tentativas -= 1
        
#         if tentativas == 0:
#             print("Usuário bloqueado")





# numero = int(input("Digite um número inteiro positivo: "))

# # Inicializa a soma dos números pares
# soma_pares = 0

# # Verifica se o número inserido é positivo
# if numero > 0:
#     # Calcula a soma dos números pares de 2 até o número inserido
#     for i in range(2, numero + 1, 2):
#         soma_pares += i

#     # Exibe o resultado
#     print(f"A soma dos números pares de 2 até {numero} é: {soma_pares}")
# else:
#     print("Por favor, insira um número inteiro positivo.")

#     numero = int(input("Digite um número inteiro: "))

# # Exibe a tabuada de multiplicação do número inserido de 1 a 10
# if numero >= 0:  # Verifica se o número é não negativo
#     print(f"\nTabuada de multiplicação do {numero}:\n")
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")
# else:
#     print("Por favor, insira um número inteiro não negativo.")





# for numero in range(99, 0, -2):
#     print(numero)

# n = int(input("digite seu numero"))
# c= 0

# r = n * c
# print(f'{n}X{c}= {r}')
# c += 1

# num =0
# print("jogo adivinha")
# chute = int(input("digite seu chute"))
# while num <=3:
#     numerodaMaquina = random.randint(1,9999)
    

#     if chute == numerodaMaquina:
#         print(f"voce ta certo seu numero é {numerodaMaquina}")
#         break
#     else:
#         print(f"vc ta errado, numro da maquina é {numerodaMaquina}")

#==========================================================================================================================================


# chance = 2

# while chance >= 0:
#     chute = int(input("digite o numero"))
#     num = random.randint(1,10)
#     if chute == num:
#         print("numero certo")
#         break

#     else:
#         print("numero erradp")
#         chance -= 1     

   

# numero_aleatorio = random.randint(5, 10)
# print(numero_aleatorio)


numeros_aleatorios = [random.randint(1, 100) for i in range(3)]
print("3 números aleatórios:", numeros_aleatorios)


numero_aleatorio_3 = random.randrange(10, 31)
print(numero_aleatorio_3)
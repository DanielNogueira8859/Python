# #----------------------------------------------------------------------------------
# print('digite um numero')
# idade1 = 45
# print('digite um numero')
# idade2 = 18

# if idade1 >= idade2:
#     print("A primeira idade é maior.")
# elif idade1 < idade2:
#     print("A segunda idade é maior.")
# else:
#     print("As idades são iguais.")
# #----------------------------------------------------------------------------------
# idade_cliente = int(input("Digite a idade do cliente: "))

# if idade_cliente < 18:
#     print("Desculpe, entrada permitida apenas para maiores de 18 anos.")
# else:
#     print("Bem-vindo ao show!")
# #----------------------------------------------------------------------------------

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))

# media  = nota1 + nota2 + nota3
# media = media/3

# if media > 6.0:
#     print('vc passou',media)

# else:
#     print('vc nao passou, pq sua média foi',media)
#-----------------------------------------------------------------------------------------
# var1=  123
# var2 ='World'
# print("Hello to the", var2, var1)

# var1 =  123
# var2 = 'World'
# print("Hello to the %s %d "%(var2, var1))

# var1 = 123
# var2 = 'World'
# print("Hello to the {}".format(var2, var1))

# var1= 123
# var2 = 'World'
# print("Hello to the " + var2+ str(var1))

# var1 =123
# var2 ='World'
# print (f"Hello to the {var2} {var1} ")

#------------------------Exercício 1: Verificação de Número Positivo---------------------
# print("digite um numero")
# numero = int(input('digite o seu numero'))

# if numero > 0:
#     print("numero maior que zero")
# elif numero <= 0:
#     print("numero menor que zero ou igual a zero")

# else:
#     print("numero invalido")


#---------------------Exercício 2: Classificação de Triângulos------------------------------

# medida1= int(input("digite a medida"))
# medida2= int(input("digite a medida"))
# medida3= int(input("digite a medida"))

# equilatero = medida1 or medida2 or medida3



# if medida1 == medida2 and medida1 == medida3 and medida2 == medida1 and medida2== medida3 and medida3 == medida1 and medida3 == medida2 :
#     print("seu triangulo é equilátero")


# elif medida1 != medida2 and medida1 !=medida3 and medida2 != medida1 and medida2 != medida3 and medida3 != medida1 and medida3 != medida2 :
#     print("seu triangulo é escaleno")

# elif medida1 or medida2 or medida3 != medida1 or medida1 or medida2 or medida3 != medida2 or medida1 or medida2 or medida3 != medida3:
#     print("seu triangulo é isósceles")

# else :
#     print("Seu triangulo nao sei qual é ")
    
#--------------------------------------Metodos----------------------------------------------
#len = comprimento
# text = "hello word"

# comprimento = len(text)
# print(comprimento)

# #type

# nuber = 100
# tipo = type(nuber)
# print(tipo)


# #conversao

# n1 = '10'
# n2 =15.0
# n3 = 25

# print("------------------------------------------------------")

# v1 = int(n1)
# print(type(v1))

# v2=  str(n2)
# print(type(v2))

# v3 = float(n3)
# print(type(v3))
#----------------------------------------------------------------------------------------------


text = "ola mundo"
lista = list(text)
print(lista)
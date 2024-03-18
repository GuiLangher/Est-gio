"""3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____

Respostas:"""

"""a) 1, 3, 5, 7, 9, 11, 13, 15
A sequencia sobe de 2 em 2"""

print("A)")
numero = 1
while numero <= 12:
        print(numero)
        numero += 2

print("-------------------------------------------")

"""b) 2, 4, 8, 16, 32, 64, 128, 256
A sequencia sobe multiplicando por 2"""

print("B)")
numero1 = 2
while numero1 <= 128:
        print(numero1)
        numero1 *= 2

print("-------------------------------------------")

"""c) 0, 1, 4, 9, 16, 25, 36, 49, 64, 81
A sequencia é os numeros inteiros consecutivos (1, 2, 3, 4, 5, 6) ao quadrado"""

print("C)")
numero2 = 0
while numero2 <= 10:
        quadrado = numero2 ** 2
        print(quadrado)
        numero2 += 1

print("-------------------------------------------")

"""d) 4, 16, 36, 64, 100, 144,
A sequencia é os numeros inteiros consecutivos multiplos de 2 (2,4,6,8,10) elevados ao quadrado"""

print("D)")
numero3 = 2
while numero3 <= 18:
        quadrado = numero3 ** 2
        print(quadrado)
        numero3 += 2

print("-------------------------------------------")

"""e) 1, 1, 2, 3, 5, 8,
A seguencia é a soma dos dois anteriores"""

print("E)")
fibonacci = [1, 1]

limite = 70

while fibonacci[-1] <= limite:
   
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    
    fibonacci.append(proximo_numero)

fibonacci.pop()

print("Sequência de Fibonacci até", limite, ":", fibonacci)

"""A atividade (e) precisei de ajuda do chat, pois tem elementos que ainda não sabia como utilizar"""

print("-------------------------------------------")

"""f) 2,10, 12, 16, 17, 18, 19,"""
"""5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;"""

def frase_invertida(string):
    return string[::-1]

frase = input (str("Digite uma frase: "))

inverter_frase = frase_invertida(frase)
print("Frase invertida", inverter_frase)
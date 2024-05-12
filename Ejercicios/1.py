# Random , MAX, SUM , / , LEN
# Random es una función que genera un número aleatorio
import random

def aletorio_numero(numero):
    numeros = [random.randint(10,100) for _ in range(numero)]
    print("Números generados", numeros)
    print(max(numeros))
    print(sum(numeros) / len(numeros))

aletorio_numero(12)
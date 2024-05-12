# Random , MAX, SUM , / , LEN
# Random es una función que genera un número aleatorio
import random
def aletorio_numero():
    numeros = [i for i in range(10,50) if i % 2 == 0 ]
    random.shuffle(numeros)
    print("Números generados", numeros[:5])
    print(max(numeros[:5]))
    print(sum(numeros[:5]) / len(numeros[:5]))

aletorio_numero()

import random
# 

def calcula_precio(precios):
    print("Lista de precios ", precios)
    precio_finales = [ (precio * 0.18)  for precio in precios]
    print(precio_finales)
    for xd in range(5):
        print(f" Articulo: {precio_finales[xd]:.2f} ")



precios = [random.randint(1,100) for _ in range(5)]
calcula_precio(precios)
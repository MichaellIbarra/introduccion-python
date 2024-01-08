def sumar(op1, op2):
    return print(f"El resultado de tu suma es : {op1 + op2}")


def restar(op1, op2):
    print(f"El resultado de tu resta es : {op1 - op2}")

def dividir(op1, op2):
    if (op2 == 0):
        print("No se puede dividir entre 0")
        return
    print(f"El resultado de tu division es : {op1 / op2}")
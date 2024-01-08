


"""#! ERRORES Y EXCEPCIONES
div = 5
divi = 0
div / divi 

def restar(num, num2):
    return num - num2


def dividir(num, num2):
    try:
        return num / num2
    except ZeroDivisionError:
        print('no se puede dividir por cero')
        return 'operación invalida'


def multiplicar(num, num2):
    return num * num2


def sumar(num, num2):
    return num + num2


try:
    a = int(input('ingrese el primer número'))
    b = int(input('ingrese el segundo número'))
    calculadora = input('Que operador aritmetico deseas usasr: +, *, /, -')
    if calculadora == '+':
        print(sumar(a, b))
    elif calculadora == '-':
        print(restar(a, b))
    elif calculadora == '*':
        print(multiplicar(a, b))
    elif calculadora == '/':
        print(dividir(a, b))
    else:
        print('opción no valida')
except:
    print('no es un numero')
print('linea nueva') """


""" #! EXCEPCIONES MULTIPLES
while True:
    try:
        c = int(input('ingrese un valor:'))
        c/0
    except ZeroDivisionError:
        print('no se puede dividir entre 0')
    except ValueError:
        print('no se puede usar letras')
    except Exception as c:
        print('no se puede dividir ',type(c).__name__) """
        
#! EJEMPLOS


try:
    valor=10/0
except ZeroDivisionError:
    print('no se puede dividir entre 0')


try:  
    miLista = [1,2,3,4,5]
    miLista[7]
except IndexError:
    print('no se puede acceder a una posición fuera de la lista')
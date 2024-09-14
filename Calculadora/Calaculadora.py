

def somar(num1, num2):
    return num1 + num2;

def sub(num1, num2):
    return num1 - num2;

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1/num2

operacoes = ["+", "-", "*", "/"]

def calculadora():
    print("Calculadora:")
    num1 = float(input("Digite o primeiro numero: "))
    op = input("Digite a operacao: ")
    if op not in operacoes:
        print("Operacao invalida")
        return

    num2 = float(input("Digite o segundo numero: "))

    match op:
        case '+':
            print(somar(num1, num2))
        case "-":
            print(sub(num1, num2))
        case "*":
            print(multi(num1, num2))
        case "/":
            print(div(num1, num2))

                
calculadora()

def celsiusFahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheitCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Selecione a conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

choice = input("Digite o número da conversão desejada (1/2): ")

if choice == '1':
    celsius = float(input("Digite a temperatura em Celsius: "))
    print("Temperatura em Fahrenheit:", celsiusFahrenheit(celsius))
elif choice == '2':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print("Temperatura em Celsius:", fahrenheitCelsius(fahrenheit))
else:
    print("Escolha inválida")
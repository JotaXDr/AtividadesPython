limite_inferior = float(input("Digite o limite inferior do intervalo: "))
limite_superior = float(input("Digite o limite superior do intervalo: "))
decremento = float(input("Digite o decremento: "))

print("Celsius\tFahrenheit")
while limite_superior >= limite_inferior:
    celsius = limite_superior
    fahrenheit = (celsius * 9/5) + 32
    print("{:.1f}\t{:.1f}".format(celsius, fahrenheit))
    limite_superior -= decremento

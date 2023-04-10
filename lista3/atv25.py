
limite_sup = float(input("Informe o limite superior do intervalo (em graus Fahrenheit): "))
incremento = float(input("Informe o incremento (em graus Fahrenheit): "))

limite_inf = 10.0

print("Fahrenheit\tCelsius")

for f in range(int(limite_inf), int(limite_sup)+1, int(incremento)):
    c = (f - 32) * 5/9
    print("{:.1f}\t\t{:.1f}".format(f, c))

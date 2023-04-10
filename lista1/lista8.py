import math

PI = math.pi

raio = float(input("Digite o raio do círculo: "))

circunferencia = 2 * PI * raio
area = PI * raio ** 2

print(f"Circunferência: {circunferencia:.2f}")
print(f"Área: {area:.2f}")

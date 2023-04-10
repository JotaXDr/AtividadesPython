josberanilson_altura = 1.5
apricocildo_altura = 1.1
anos = 0

while apricocildo_altura <= josberanilson_altura:
    anos += 1
    josberanilson_altura += 0.02
    apricocildo_altura += 0.03
    print(f"Ano {anos}: Josberanilson {josberanilson_altura:.2f}m, Apricoçildo {apricocildo_altura:.2f}m")

print(f"Apricoçildo ultrapassou Josberanilson após {anos} anos.")

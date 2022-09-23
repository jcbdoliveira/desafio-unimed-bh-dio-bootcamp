#Calculo da distancia do ICM da terra média
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

print(f"{distancia / (diametro1 + diametro2):.2f}")




#Cálculo de distancia e consumo de combustivel
valores = input().split() 

horas = int(valores[0])
velocidade_media = int(valores[1])
distancia = (velocidade_media * horas) 
consumo = distancia / 12

print(f"{consumo:.3f}")
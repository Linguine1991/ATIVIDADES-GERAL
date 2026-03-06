#Quadrados de 1 a 10
quadrados = [x**2 for x in range(1,10)]
print("Quadrados: ", quadrados)

pares = [x for x in range(1,21) if x % 2 == 0]
print("Pares: ", pares)

#Vogais de "PROGAMACAO"
vogais  = [letra for letra in "PRAGAMACAO" if letra in "AEIOU"]
print("Vogais: ", vogais)
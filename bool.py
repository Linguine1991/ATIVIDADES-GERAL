#resp = input("voce va passar de ano? s/n:")
#resultado = bool(resp)

#print("resultado", resp)
#print("resultado ", resultado )

resp = input("Você vai passar de ano? s/N: ").strip( ).lower()

#resultado = (resp =="S")
resultado = resp in ("s", "sim")

print("resultado ", resultado)
print(type(resultado))
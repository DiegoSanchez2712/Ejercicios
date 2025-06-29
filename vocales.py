pedir = input("Digite una palabra: ")
vocales = {"a":0, "e":0, "i":0, "o":0, "u":0}

for i in pedir:
    i = i.lower()
    if i in vocales:
        vocales[i] +=1

for i,j in vocales.items():
    print(f"la {i} se repitio {j} veces")

asignaturas = ["Matematicas", "Ciencias naturales", "Castellano", "Quimica", "Fisica"]
notas = []

for i in asignaturas[:]:
    r = float(input(f"Digite la nota que saco e {i}"))
    if r >= 3:
        notas.append(r)
    else:
        asignaturas.remove(i)
print("---------------------------------------------")    
for i in range(len(asignaturas)):
    print(f"{asignaturas[i]}: {notas[i]}")
    
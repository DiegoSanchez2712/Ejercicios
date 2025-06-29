import random
puntuacion = 0
perdidas = 0
verificador = True

while True:
    cartaB = random.randint(1,13)
    cartaJ = random.randint(1,13)
    jugar = int(input(f"La carta es {cartaJ}.\n1. Si \n2. No \nDesea jugarla?"))
    
    if jugar == 1:
        if cartaJ > cartaB:
            puntuacion += 1
            print(f"El ususario tiene una carta mayor que el bot, con una puntuacion actual de {puntuacion}")

        elif cartaJ < cartaB:
            perdidas +=1
            print(f"El usuario ha perdido, {perdidas}/3 veces")
        elif cartaJ == cartaB:
            print("El usuario tiene la misma carta que el bot, no se le suma puntuacion ")

    elif jugar == 2:
        continue
    else:
        print("Digite una opcion valida")
    if perdidas == 3:
        print(f"El usuario perdio, con un puntuacion de {puntuacion}")
        break
    elif puntuacion == 5:
        print(f"El usuario gano, perdio {perdidas} veces")
        break









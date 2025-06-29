import random
jugador = 0
bot = 0
ronda = False
numR = 1
opciones = ["Piedra", "Papel", "Tijeras"]

# 1.piedra 2. papel 3.tijera
while numR <6:
    opcionJ = int(input(f"1. Piedra \n2. Papel \n3. Tijeras \nDIgite la opcion que va a jugar en la ronda {numR}: "))
    opcionB = random.randint(1,3)
    print(f"{opciones[opcionJ-1]} contra {opciones[opcionB-1]}")
    if opcionJ == opcionB:
        print(f"empate, no hay puntos ({jugador}-{bot})")
        continue

    elif opcionJ == 1:
        if opcionB == 2:
            bot += 1
        else:
            jugador +=1
            ronda = True

    elif opcionJ == 2:
        if opcionB == 3:
            bot += 1
        else:
            jugador +=1
            ronda = True

    elif opcionJ == 3:
        if opcionB == 1:
            bot += 1
        else:
            jugador += 1
            ronda = True
    
    else:
        print("Opcion no valida")
        continue
    
    if ronda == False:
        print(f"Ronda a favor del bot ({jugador}-{bot})")
    else:
        print(f"Ronda a favor del jugador ({jugador}-{bot})")
    numR += 1

else:
    print(f"Tabla final: {jugador}-{bot}")
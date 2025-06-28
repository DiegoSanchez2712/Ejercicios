total = 0

while True: 
    pedir = int(input("1. Te(3500) \n2. Jugo(3000) \n3. Refresco(2500) \n0. Salir \nDigite la bebida que desea: "))

    if pedir == 1:
        total += 3500
        print(f"Te sumado al total, con un total de {total}")
    
    elif pedir == 2:
        total += 3000
        print(f"Jugo sumado al total, con un total de {total}")
    
    elif pedir ==3:
        total += 2500
        print(f"Refresco sumado al total, con un total de {total}")

    elif pedir == 0:
        if total == 0:
            print("No se realizaron compras")
            break
        else: 
            print(f"compra realizada, su total a pagar es de {total}")
            break
    else:
        print("Digite una opcion valida")


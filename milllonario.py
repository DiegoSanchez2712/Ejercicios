import random
preguntas = {
    1: [
        {"pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["A. Oceano Pacifico", "B. Oceano Atlantico", "C. Oceano Indico", "D. Oceano Artico"],
        "respuesta" : "A"},
                
        {"pregunta": "¿En qué continente se encuentra Egipto?",
        "opciones": ["A. Europa", "B. America", "C. Africa", "D. Asia"],
        "respuesta" : "C"}],
                  
    2 : [
        {"pregunta": "¿Quién escribió Don Quijote de la Mancha?",
         "opciones": ["A. Pablo Picasso" , "B. Miguel de Cervantes", "C. William Shakespeare", "D. Gabriel García Márquez"],
         "respuesta": "B"},

        {"pregunta": "¿Qué planeta es conocido como el planeta rojo?",
         "opciones": ["A. Tierra", "B. Jupiter", "C. Saturno", "D. Marte"],
         "respuesta": "D"}],

    3: [
        {"pregunta": "¿Cuál es la capital de Canadá?",
        "opciones": ["A. Ottawa", "B. Washington", "C. Paris", "D. Berlin"],
        "respuesta" : "A"},
                
        {"pregunta": "¿Cual es el organo más grande del cuerpo humano?",
        "opciones": ["A. Corazón", "B. Pancreas", "C. Piel", "D. Higado"],
        "respuesta" : "C"}],
    4: [
        {"pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "opciones": ["A. 1965", "B. 1932", "C. 1912", "D. 1939"],
        "respuesta" : "D"},
                
        {"pregunta": "¿Cuál es el elemento químico cuyo símbolo es Fe?",
        "opciones": ["A. Hierro", "B. Oro", "C. Hidrogeno", "D. Oxigeno"],
        "respuesta" : "A"}],
        
    5: [
        {"pregunta": "¿Quién pintó La escuela de Atenas?",
        "opciones": ["A. Leonardo da vinci", "B. Rafael Sanzio", "C. Diego vasquez", "D. Francisco de Goya"],
        "respuesta" : "B"},
                
        {"pregunta": "¿Qué filósofo griego fue maestro de Aristóteles?",
        "opciones": ["A. Homero", "B. Sócrates", "C. Platón", "D. Tales de Mileto"],
        "respuesta" : "C"}],
    6: [
         {"pregunta": "¿Que isla es la mas grande en el mundo?",
        "opciones": ["A. Groenlandia ", "B. Nueva Guinea ", "C. Madagascar. ", "D. Honshu"],
        "respuesta" : "A "},

         {"pregunta": "¿Cuál es el río más largo de África?",
          "opciones": ["A. Amazonas", "B. Misisipi ", "C. Nilo", "D. Obi"],
          "respuesta": "C"}],

    7: [
         {"pregunta": "¿Cual es la obra más famosa de Victor Hugo?",
        "opciones": ["A. Los trabajadores del mar ", "B. Las orientales", "C. Nuestra señora de París ", "D. Las miserables"],
        "respuesta" : "D"},

         {"pregunta": "¿Qué teoría científica desarrollaron de forma independiente Newton y Leibniz?",
          "opciones": ["A. El cálculo infinitesimal", "B. Ley de la gravitación universal", "C. Ley de la inercia", "D. La luz"],
          "respuesta": "A"}],

    8: [
         {"pregunta": "¿En qué año cayó el Imperio Romano de Occidente?",
        "opciones": ["A. 400 d.C", "B. 476 d.C", "C. 458 d.C", "D. 502 d.C"],
        "respuesta" : "B"},

         {"pregunta": "¿En que fecha ocurrio la Revolución Industrial?",
          "opciones": ["A. 1687", "B. 1915", "C. 1760", "D. 1789"],
          "respuesta": "C"}],

    9: [
         {"pregunta": "¿Qué país tiene como moneda oficial el dólar namibio?",
        "opciones": ["A. Afghanistan", "B. Namibia", "C. Escocia", "D. Paises bajos"],
        "respuesta" : "B"},

         {"pregunta": "¿Cuál es el nombre del manuscrito ilustrado medieval de contenido botánico y astronómico que aún no ha sido descifrado?",
          "opciones": ["A. el Libro de Kells", "B. Manuscritos del Mar Muerto", "C. Códice Crosby-Schøyen", "D. Manuscrito Voynich"],
          "respuesta": "D"}],

    10: [
         {"pregunta": "¿Cuál es el nombre del teorema matemático que establece que no existen soluciones enteras positivas para la ecuación an+bn=cn cuando n>2?",
        "opciones": ["A. Teorema de pitagoras", "B. Último Teorema de Fermat", "C. Teorema Fundamental del Cálculo", "D. Teorema de Tales"],
        "respuesta" : "B"},

         {"pregunta": "¿Qué físico propuso la hipótesis del multiverso dentro del marco de la teoría cuántica de los muchos mundos?",
          "opciones": ["A. Hugh Everett III", "B. Niels Bohr", "C. Max Planck", "D. Max Born"],
          "respuesta": "A"}],

    }

nombre = input("\n¡BIENVENIDO A... QUIEN QUIERE SER MILLONARIO!\nIngrese su nombre: ")
opciones = ["A", "B", "C", "D"]
comodines = [True, "1. Llamada a un amigo", True, "2. 50/50", True, "3. Cambiar de pregunta"]
salir = False
total = 0

for num_pregunta, conjunto in preguntas.items():
    opciones_mitad = []

    def llamada():
        if comodines[0]:
            print(f"hmm... yo creo que es la {random.choice(elegida['opciones'])}")
            comodines[0] = False
        else:
            print("\n[!] Opcion ya utilizada")

    def mitad_opciones():
        if comodines[2]:
            print("\n[50/50 activado]")
            opcion_correcta = next(op for op in elegida["opciones"] if op.startswith(elegida["respuesta"] + "."))
            incorrectas = [op for op in elegida["opciones"] if not op.startswith(elegida["respuesta"] + ".")]
            opcion_incorrecta = random.choice(incorrectas)
            elegida["opciones"] = [opcion_correcta, opcion_incorrecta]
            random.shuffle(elegida["opciones"])
            for op in elegida["opciones"]:
                print(op)
            comodines[2] = False
        else:
            print("\n[!] Opcion ya utilizada")

    def cambio():
        if comodines[4]:
            nueva = preguntaElegida[0]
            comodines[4] = False
            return nueva
        else:
            print("\n[!] Opcion ya utilizada")
            return None

    preguntaElegida = conjunto.copy()
    aleatoriedad = random.randint(0, 1)
    elegida = preguntaElegida.pop(aleatoriedad)

    print(f"\n{nombre}, Pregunta {num_pregunta}:\n{elegida['pregunta']}")
    for op in elegida["opciones"]:
        print(op)

    while True:
        comodin = input("\n------------------------------------\n¿Desea utilizar un comodín?:\n1. Si\n2. No\nRespuesta")
        if comodin == "1":
            for i in range(0, len(comodines), 2):
                estado = "[DISPONIBLE]" if comodines[i] else "[USADO]"
                print(f"{comodines[i+1]} {estado}")
            eleccion = input("Elija el número del comodín (1-3): ")
            if eleccion == "1": llamada()
            elif eleccion == "2": mitad_opciones()
            elif eleccion == "3":
                nueva_pregunta = cambio()
                if nueva_pregunta:
                    elegida = nueva_pregunta
                    print(f"\nNueva pregunta {num_pregunta}:\n{elegida['pregunta']}")
                    for op in elegida['opciones']:
                        print(op)
        elif comodin == "2":
            break
        else:
            print("[!] Opcion invalida")

    while True:
        user_input = input("\nDigite la opción (A, B, C, D): ").upper()
        opciones_validas = [op[0] for op in elegida["opciones"]]

        if user_input in opciones_validas:
            if user_input == elegida["respuesta"]:
                print("\nCorrecto!")
                total += 100000
            else:
                print("\nIncorrecto. Fin del juego.")
                salir = True
            break
        else:
            print("[!] Opcion no disponible. Intenta otra.")

    if salir:
        break

    while True:
        asegurar = input(f"\n¿Desea retirarse con ${total}?\n1. Sí\n2. No\nOpcion: ")
        if asegurar == "1":
            print(f"\n{nombre} se ha retirado con ${total}.")
            salir = True
            break
        elif asegurar == "2":
            print(f"\n{nombre} decide continuar. Total acumulado: ${total}.")
            break
        else:
            print("[!] Ingrese una opción válida")

print(f"\nJuego terminado. Total ganado: ${total}") 


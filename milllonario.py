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
nombre = input("¡BIENVENIDO A... QUIEN QUIERE SER MILLONARIO! \nIngrese su nombre: ")
opciones = ["A", "B", "C", "D"]
comodines = [True,"1. Llamada a un amigo", True, "2. 50/50", True,"3. Cambiar de pregunta"]
salir = False
total = 0

for i,j in preguntas.items():
    def llamada():
        if comodines[0] == True:
            print(f"hm... yo creo que es la {elegida["opciones"][random.randint(0,3)]}")
            comodines[0] = False
        else: 
            print("Opcion ya utilizada")

    def mitad_opciones():
        if comodines[2] == True:
            for i in range(len(elegida["opciones"])):
                if elegida["respuesta"] == opciones[i]:
                    print(elegida["pregunta"])
                    print(elegida["opciones"].pop(i))
                    print(elegida["opciones"][random.randint(0,2)])
                    comodines[2] = False
        else:   
            print("Opcion ya utilizada")
    def cambio():
        if comodines[4] == True:
            elegida =  preguntaElegida[0] 
            print(f"La nueva pregunta numero {i} es : \n{elegida["pregunta"]}")
            for k in elegida["opciones"]:
                print(k)
            comodines[4] = False
        else:
            print("Opcion ya utilizada")
            
    preguntaElegida = [j[0], j[1]]
    aleatoridad = random.randint(0,1)
    elegida = preguntaElegida[aleatoridad]
    preguntaElegida.pop(aleatoridad)   
    print(f"{nombre}, La pregunta numero {i} es : \n{elegida["pregunta"]}")

    for k in elegida["opciones"]:
        print(k)
    while True:   
        comodin =  int(input("---------------------------- \n1. si \n2. no \nDesea utilizar comodin?: "))
    
        if comodin == 1:
            for i in range(len(comodines)):
                if i % 2 == 0:
                    if comodines[i] == True:
                        print(comodines[i+1])
                    else:
                        print(f"{i+1}. Opcion utilizada")
                else: 
                    continue
            comodin_eleccion =  int(input("Elija el comodin: "))
            if comodin_eleccion == 1:
               llamada()
            elif comodin_eleccion == 2:
                mitad_opciones()
            elif comodin_eleccion == 3:
                cambio()
        elif comodin == 2:
            break
        else:
            print("Digite una opcion correcta")    
    
    while True:
        user_eleccion = input("Digite la opcion indicada: ")
        for i in range(len(opciones)):
            if user_eleccion.upper() in opciones:   
                if user_eleccion.upper() == elegida["respuesta"]:
                    total += 100000
                    print("haz acertado")
                    break
                else:
                    print("perdio")
                    salir = True
                    break
                    
            else:
                print("Digite una opcion correcta")

        if salir == True:
            break
        while True:
            asegurar = int(input(f"\n1. si \n2. no \nDesea llevarse solo {total}?:  "))
            if asegurar == 1:
                print(f"El usuario se ha plantado con {total}")
                salir = True
                break   
            elif asegurar == 2:
                print(f"El usuario no se desea plantar. su dinero acumulado actualmente es {total}")
                break
            else:
                print("¡Digite una opcion valida!")
        break

    if salir == True:
            break  
    
else:
    print(f"haz ganado las 10 preguntas, con un total neto de {total}")
    


# Importar las preguntas desde el archivo preguntas.py
from preguntasDiccionario import preguntas
#no documento el codigo ya que yo mismo lo voy a explicar

def iniciar_juego():
    puntaje = 0
    total_preguntas = len(preguntas) 
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)

        respuesta_usuario = input("Selecciona una opción (a, b, c): ")

        
        if(respuesta_usuario == pregunta["respuesta"]):
            print("respuesta correcta")
            puntaje += 1;
        else:
           print("Respuesta incorrecta, la correcta es: ",pregunta["respuesta"])
        print()

    
    print("Repuestas correctas ",puntaje,"de ",total_preguntas)

    porcentaje_correctas = (puntaje / total_preguntas) * 100
    
    
    if porcentaje_correctas >= 60:
        print("Aprobaste tu puntaje es de: ",porcentaje_correctas)
    elif porcentaje_correctas == 100:
        print("Respondiste todas correctamente")
    else:
        print(f"Desaprobado. Tu puntaje es {porcentaje_correctas:.2f}%")


def menu_principal():
    while True:
        print("Bienvenido al Quiz")
        print("1. Iniciar Juego")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        
        if opcion == "1":
            iniciar_juego()
        elif opcion == "2":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

menu_principal()
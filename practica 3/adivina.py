import random

def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

while True:
    print("¿El número resultante será par o impar? (Escribe 'salir' si deseas terminar)")
    elección_usuario = input().lower()

    if elección_usuario == "salir":
        break

    resultado_dados = tirar_dados()
    print("Los dados sumaron:", resultado_dados)

    es_par = resultado_dados % 2 == 0

    if (elección_usuario == "par" and es_par) or (elección_usuario == "impar" and not es_par):
        print("¡Ganaste la ronda!")
    else:
        print("Perdiste. Sigue intentando.")

# 1. Función básica sin parámetros
def saludar():
    print("Hola, terrícola")

# Llamada a la ejecución de la función
saludar()

# 2. Función con paso de parámetros
def saludar_persona(nombre):
    print("Hola", nombre)

saludar_persona("Rodrigo")

# 3. Función que procesa operaciones matemáticas y retorna un valor
def convertir_celsius_fahrenheit(celsius):
    resultado = (celsius * 9/5) + 32
    return resultado

# Captura y asignación del valor de retorno en una nueva variable
temperatura_f = convertir_celsius_fahrenheit(25)
print("Temperatura en Fahrenheit:", temperatura_f)

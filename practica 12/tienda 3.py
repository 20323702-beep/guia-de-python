print("*********************************")
print("          Bienvenido a           ")
print("       La tienda de mascotas     ")
print("*********************************")

num_perros = 10
num_gatos = 8
num_pájaros = 25

print("Por favor, ingresa tu nombre")
nombre = input()

print("Por favor, escribe tu apellido")
apellido = input()

# Concepto de concatenación (sumar textos)
nombre_completo = nombre + " " + apellido 

print("Actualmente contamos con")
print("Perros:", num_perros, "Gatos:", num_gatos, "Pájaros:", num_pájaros)

animales_totals = num_perros + num_gatos + num_pájaros

print("En total tenemos", animales_totals, "animales")

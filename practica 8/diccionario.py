# Declaración de un diccionario (usando llaves y formato llave-valor)
persona = {
    "nombre": "Rodrigo",
    "edad": 30,
    "ciudad": "México"
}
print(persona)

# Acceso directo a los valores utilizando el nombre de su llave
print(persona["nombre"])
print(persona["edad"])

# Modificar o actualizar el valor de una llave existente
persona["edad"] = 31

# Insertar un nuevo par de llave-valor
persona["profesión"] = "Programador"
print(persona)

# Eliminar una llave utilizando la instrucción del sistema del
del persona["ciudad"]
print(persona)

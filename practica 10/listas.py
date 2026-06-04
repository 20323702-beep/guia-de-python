# Inicialización de una lista (mutable usando corchetes)
nombres = ["Rodrigo", "Juan", "Pedro"]
print(nombres)

# Lectura de componentes específicos por medio de su índice numérico
print(nombres[0])  # Devuelve el primer elemento ("Rodrigo")
print(nombres[1])  # Devuelve el segundo elemento ("Juan")

# Adición de nuevos elementos dinámicos mediante el método .append()
nombres.append("María")
print(nombres)

# Eliminación de elementos por su valor empleando el método .remove()
nombres.remove("Juan")
print(nombres)

# Inicialización de una tupla (inmutable usando paréntesis)
coordenadas = (10, 20)
print(coordenadas)

print ("Sistema para calcular el promedio de un alumno.")

nombre = input("para comenzar, ¿cual es tu nombre?: ")

matematicas = int(input(nombre + " ¿cual es tu calificacion en matematicas?: "))
quimica = int(input(nombre + " ¿cual es tu calificacion en quimica?: "))
biologia = int(input(nombre + " ¿cual es tu calificacion en biologia?: "))
ingles = int(input(nombre + " ¿cual es tu calificacion en ingles?: "))
lengua_castellana = int(input(nombre + " ¿cual es tu calificacion en lengua castellana?: "))

promedio = (matematicas + quimica + biologia + ingles + lengua_castellana) / 5
promedio = int(promedio)

if promedio >= 7:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)

print("Fin.")

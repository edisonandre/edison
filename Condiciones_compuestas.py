print ("sistema para calcular el promedio de un alumno.")

nombre = input("para comenzar, ¿cual es tu nombre?: ")

matematicas = float(input(nombre + "¿cual es tu calificacion en matematicas?: "))
quimica = float(input(nombre + "¿cual es tu calificacion en quimica. "))
biologia = float(input(nombre + "¿cual es tu calificacion en biologia. "))
ingles = float(input(nombre + "¿cual es tu calificacion en ingles. "))
etica = float(input(nombre + "¿cual es tu calificacion en etica. "))

promedio = (matematicas + quimica + biologia + ingles + etica) / 5

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,3))
else:
    print("LO  sentimos " + nombre + " has 'reprobado' con un promedio de: ", promedio)
    print("LO  sentimos " + nombre + " has 'reprobado' con un promedio de: ", round(promedio, 1))


print("Fin.")      
    

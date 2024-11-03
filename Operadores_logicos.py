#conjucion

print ("conjuncion (and)")

num_uno = int(input("Escribe un numero mayor a 2 y menor a 5:"))

if num_uno > 2 and num_uno < 5:
    print("El numero ", num_uno, " cumple con la condicion.\n")
else:
    print("El numero ", num_uno, " No cumple con la condicion.\n")

#disyuncion
print("Disyuncion (or)")

palabra = input("para cumplir con la condicion escribe 'si' o 'yes':")

if palabra == "si" or palabra == "yes":
    print("La condicion se ha cumplido.\n")
else:
    print("La condicion No se ha cumplido.\n")

#Negacion
print("Negacion (not)")

num_uno = int(input("Intruduce un numero igual a 5: "))

if not num_uno == 5:
    print("\n El numero es diferente de cinco y si cumple la condicion.\n")
else:
    print("\n El numero es igual a cinco y No cumple la condicion.\n")





    

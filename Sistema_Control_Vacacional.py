print("***************************************")
print("* Sistema de control vacacional Rappi *")
print("*************************************** /n")

nombre_empleado = input("Por favor intruduce el nombre del empleado: ")
clave_departamento = int (input("por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor intrudice los años laboradosdel empleado: "))

if clave_departamento == 1:
    
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "Tiene derecho a 6 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 6 dias de vacaciones")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 14 dias de vacaciones")
    else:
        print("El empleado ", nombre_empleado, "aun no tiene derecho a vacaciones.")

elif clave_departamento == 2:
    
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "Tiene derecho a 7 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 15 dias de vacaciones")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 dias de vacaciones")
    else:
        print("El empleado ", nombre_empleado, "aun no tiene derecho a vacaciones.")

elif clave_departamento == 3:

    
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "Tiene derecho a 10 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 dias de vacaciones")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 30 dias de vacaciones")
    else:
        print("El empleado ", nombre_empleado, "aun no tiene derecho a vacaciones.")

else:
    print("La clave de departamento no existe, vuelve a intentarlo.")
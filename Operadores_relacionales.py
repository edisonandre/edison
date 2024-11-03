print("introduce dos numeros a comparar: \n")

num_uno = int(input("Intruduce el primer numero: "))
num_dos = int(input("Intruduce el segundo numero: "))

print ("\n Los numeros a comparar son: ", num_uno, " y ", num_dos, "\n")

if num_uno == num_dos:
    print("Es igual...")
if num_uno != num_dos:
    print("Es diferente")
if num_uno < num_dos:
    print("Es menor...")
if num_uno > num_dos:
    print ("Es mayor...")
if num_uno <= num_dos:
    print("Es menor o igual...")
if num_uno >= num_dos:
    print("Es mayor o igual...")
    

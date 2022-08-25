numero=5

'''while(numero<10):
    print("Estoy adentro de la cuerda")
    numero+=1
else:
    print("Adiooos")
print("Estoy por fuera de la cuerda")'''

opcion=1
print("****Menu*****")
print("1. SUMAR")
print("2. RESTAR")
print("0. SALIR")

while(opcion != 0):
    opcion=int(input("Digite una opcion: "))
    if(opcion==1):
        print("Sumando")
    elif(opcion==2):
        print("Restando")
    else:
        print("Digite una opcion valida")

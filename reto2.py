#Variable de control
contador=0

#contador de negaticos
contadorNegativos=0
while contador<=5:
    numero=int(input("Digita un numero: "))
    if numero<0:
        contadorNegativos+=1    
    else:
        contadorNegativos=contadorNegativos
    contador+=1
print(f'Hay {contadorNegativos} negativos ')
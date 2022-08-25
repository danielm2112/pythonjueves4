#variable de control
numero=5

#acumulador
suma=0

#declaro el ciclo
while(numero>0):
    #pedir un numero
    numero=int(input("Digite un numero: "))
    if numero >=0:
        suma=suma + numero
    else:
        print(f'La suma fue {suma}')    
        break
print(f'La suma fue {suma}')    
  


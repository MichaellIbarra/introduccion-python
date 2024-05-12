def buscar_estaciones(palabra):
    estaciones={'Nieve':'Invierno','Frío':'Invierno','Flores':'Primavera','Sol':'Verano','Calor':'Verano','Viento':'Otoño'}
    
    if palabra in estaciones:
        return estaciones[palabra]
    else:
        return None
    

while True:
    palabra=input("Ingrese la palabra: ")
    resultado = buscar_estaciones(palabra) #Invierno
    
    if resultado:
        print(resultado)
        break


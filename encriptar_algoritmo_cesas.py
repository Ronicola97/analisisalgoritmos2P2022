#sin funciones
import string 
abc = string.ascii_lowercase 
print(len(abc)) 
paso = 3 
mensaje = input("Ingrese el mensaje:") 
codificado = "" 
for i in mensaje: 
    if i in abc: 
        indice = abc.index(i) 
        nuevo = indice + paso 
        if nuevo>25: 
            nuevo = nuevo - 26 
        codificado += abc[nuevo] 
    else: 
        codificado += i 

print(f'codificado: {codificado}') 

decodi = "" 

for i in codificado: 
    if i in abc: 
        indice = abc.index(i) 
        nuevo = indice - paso 
        decodi += abc[nuevo] 
    else: 
        decodi += i 

print(f'decodificado: {decodi}')

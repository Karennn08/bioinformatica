import numpy as np
import matplotlib.pyplot as plt

################### FRACCION DE CODIGO###################
#fasta = input("Escriba el nombre de la molecula en formato fasta, eje, TP53.fasta: ")
#file = open(f'{fasta}')
file = open(f'CFTR.fasta')
rfile = file.readlines()
#LAS SIGUIENTES LINEAS CARGAN LA SECUENCIA Y LA DEJA LISTA PARA HACER CALCULOS
nombre_seq = rfile[0].strip()
secuencia = ""
for i in rfile[1:]:
        secuencia += i.strip()
#DE AQUI EN ADELANTE DEBES CONTAR LOS AMINOCIDOS QUE HAY EN TOTAL
#Y HACER UNA GRAFICA DE BARRAS DE LOS 20 AMINOACIDOS
print("\n\n")
print(secuencia)
print(f"\nEn total hay: {len(secuencia)} aminoacidos\n")

########################################################### Aminoacidos presentes
aminoacidos = []
for i in secuencia:
    if i not in aminoacidos:
        aminoacidos+=i   
print(f"\nEn la molecula hay {len(aminoacidos)} tipos de aminoacidos: {aminoacidos}\n")

########################################################## Conteo de cada tipo de aminoacido
lConteo = []
for a in aminoacidos:
    count = secuencia.count(a)
    lConteo += [[count,a]]
    #print(f"\nEl aminoacido {a} aparece {count} veces en la lista\n")
#print(lConteo)

########################################################## Hallar aminoacido de mayor y menor frecuencia
maximo = max(lConteo)
minimo = min(lConteo)
print(f"\nEl aminoacido de mayor frecuencia es {maximo[1]} con {maximo[0]} aminoacidos y el de menor frecuencia es {minimo[1]} con {minimo[0]} aminoacidos")

########################################################## Hallar porcentaje de escenciales y no escenciales
es="K,R,H,V,I,M,W,F,T,L".split(',')
noes= "A,N,D,C,Q,E,G,P,S,Y".split(',')
ces = 0
cnoes = 0
for a in es:
    ces+= secuencia.count(a)
for a in noes:
    cnoes+= secuencia.count(a)

print(f"\nEl porcentaje de aminoacidos escenciales es {ces/len(secuencia)*100} y de no escenciales es {cnoes/len(secuencia)*100}")

########################################################## HACER GRAFICA
lista_strings = []
lista_numeros = []

# Recorrer la lista original y agregar cada elemento a la lista adecuada
for elemento in lConteo:
    for x in elemento:
        if isinstance(x, str):
            lista_strings.append(x)
        elif isinstance(x, (int, float)):
            lista_numeros.append(x)

print(lista_numeros, lista_strings)

# Crear los datos de ejemplo
x = np.array(lista_strings)
y = np.array(lista_numeros)

# Crear la gráfica de barras
plt.bar(x, y)

# Añadir títulos y etiquetas a los ejes
plt.title('Conteo de aminoacidos')
plt.xlabel('Aminoacidos')
plt.ylabel('Veces en la proteina')

# Mostrar la gráfica
plt.show()